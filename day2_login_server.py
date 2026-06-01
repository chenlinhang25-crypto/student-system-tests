"""
Day 2: 本地登录接口服务

运行方式：
cd "C:/Users/陈林航/Documents/Codex/2026-05-28/new-chat"
python ./day2_login_server.py

启动后浏览器访问：
http://127.0.0.1:5000/login

注意：
浏览器直接打开 /login 会看到说明文字。
真正测试登录接口，要用 requests.post 发送 username 和 password。
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class LoginHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/login":
            self.send_json(
                200,
                {
                    "message": "登录接口已启动。请用 POST 请求，并传 username 和 password。",
                    "example": {"username": "admin", "password": "123456"},
                },
            )
            return

        self.send_json(404, {"code": 404, "message": "接口不存在"})

    def do_POST(self):
        if self.path != "/login":
            self.send_json(404, {"code": 404, "message": "接口不存在"})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length)

        try:
            data = json.loads(raw_body or b"{}")
        except json.JSONDecodeError:
            self.send_json(400, {"code": 400, "message": "请求体不是合法 JSON"})
            return

        username = data.get("username", "")
        password = data.get("password", "")

        if username == "":
            self.send_json(200, {"code": 1001, "message": "username required"})
        elif password == "":
            self.send_json(200, {"code": 1002, "message": "password required"})
        elif username == "admin" and password == "123456":
            self.send_json(200, {"code": 0, "message": "success", "token": "abc123"})
        else:
            self.send_json(200, {"code": 1003, "message": "username or password error"})

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), LoginHandler)
    print("登录接口服务已启动：http://127.0.0.1:5000/login")
    print("按 Ctrl + C 可以停止服务")
    server.serve_forever()
