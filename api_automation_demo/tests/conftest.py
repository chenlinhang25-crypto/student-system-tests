import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest


class DemoApiHandler(BaseHTTPRequestHandler):
    users = {
        "1": {"id": 1, "name": "Alice", "role": "tester"},
        "2": {"id": 2, "name": "Bob", "role": "developer"},
    }

    def _send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path.startswith("/users/"):
            user_id = self.path.rsplit("/", 1)[-1]
            user = self.users.get(user_id)
            if user:
                self._send_json(200, user)
            else:
                self._send_json(404, {"error": "user not found"})
            return
        self._send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path == "/users":
            content_length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(content_length) or b"{}")
            self._send_json(201, {"id": 3, **payload})
            return
        self._send_json(404, {"error": "not found"})

    def log_message(self, format, *args):
        return


@pytest.fixture(scope="session")
def base_url():
    server = HTTPServer(("127.0.0.1", 0), DemoApiHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
