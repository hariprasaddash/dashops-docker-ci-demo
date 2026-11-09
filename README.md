# DashOps Docker + CI Demo

A dependency-free HTTP service showing a practical Dockerization handover.

## Demonstrated
- Docker image based on `python:3.12-slim`
- Non-root runtime user
- Container health check
- Configurable port and service name
- GitHub Actions image build on push and pull request
- Gitleaks repository secret scan
- Local Docker smoke test

> Portfolio demonstration only. Review base-image updates, third-party Actions, security findings, and runtime requirements before production use.

## Run
Requires Docker Engine and curl.

```bash
docker build -t dashops-demo:local .
docker run --rm -p 8080:8080 dashops-demo:local
```

In another terminal:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
```

## Smoke test

```bash
chmod +x tests/smoke_test.sh
./tests/smoke_test.sh
```

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `PORT` | `8080` | HTTP listen port |
| `SERVICE_NAME` | `dashops-demo` | Service identifier |

## CI
The workflow builds but does not publish an image or deploy to production.

## Scope boundaries
No Kubernetes manifests, registry publishing, cloud credentials, production deployment, or automated remediation are included. These require separate requirements and approval.
