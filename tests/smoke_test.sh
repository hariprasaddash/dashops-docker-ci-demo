#!/usr/bin/env sh
set -eu

IMAGE="${IMAGE:-dashops-demo:local}"
NAME="dashops-demo-test"

cleanup() {
  docker rm -f "$NAME" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker build -t "$IMAGE" .
docker run -d --name "$NAME" -p 18080:8080 "$IMAGE" >/dev/null

i=0
until curl --fail --silent http://127.0.0.1:18080/health >/dev/null; do
  i=$((i + 1))
  if [ "$i" -ge 20 ]; then
    docker logs "$NAME"
    exit 1
  fi
  sleep 1
done

curl --fail --silent http://127.0.0.1:18080/ | grep -q '"service": "dashops-demo"'

echo "Smoke test passed"
