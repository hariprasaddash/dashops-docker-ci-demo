from http.server import BaseHTTPRequestHandler, HTTPServer
import json, os, socket
from datetime import datetime, timezone

class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            return self.send_json(200, {"status": "ok"})
        if self.path == "/":
            return self.send_json(200, {
                "service": os.getenv("SERVICE_NAME", "dashops-demo"),
                "hostname": socket.gethostname(),
                "time_utc": datetime.now(timezone.utc).isoformat(),
                "message": "Container is running"
            })
        return self.send_json(404, {"error": "not_found"})

    def log_message(self, fmt, *args):
        print(json.dumps({"level": "info", "message": fmt % args}), flush=True)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", int(os.getenv("PORT", "8080"))), Handler).serve_forever()
