"""
Day 3: 登录 + 用户信息接口服务
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

USERS = {
    "admin": {"username": "admin", "password": "123456", "role": "admin", "email": "admin@example.com", "department": "技术部"},
    "test": {"username": "test", "password": "test123", "role": "tester", "email": "test@example.com", "department": "测试部"},
}

TOKEN_STORE = {}

class APIHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def get_request_body(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(content_length)
        try:
            return json.loads(raw_body or b"{}")
        except json.JSONDecodeError:
            return None

    def get_token_from_header(self):
        auth_header = self.headers.get("Authorization", "")
        if auth_header.startswith("Bearer "):
            return auth_header[7:]
        return None

    def do_GET(self):
        if self.path == "/login":
            self.send_json(200, {"message": "登录接口", "example": {"username": "admin", "password": "123456"}})
        elif self.path == "/user_info":
            token = self.get_token_from_header()
            if not token:
                self.send_json(401, {"code": 401, "message": "未提供 token"})
                return
            username = TOKEN_STORE.get(token)
            if not username:
                self.send_json(401, {"code": 401, "message": "token 无效"})
                return
            user = USERS.get(username)
            if user:
                self.send_json(200, {"code": 0, "message": "success", "data": {"username": user["username"], "role": user["role"], "email": user["email"], "department": user["department"]}})
        else:
            self.send_json(404, {"code": 404, "message": "接口不存在"})

    def do_POST(self):
        if self.path == "/login":
            data = self.get_request_body()
            if data is None:
                self.send_json(400, {"code": 400, "message": "JSON 解析失败"})
                return
            username = data.get("username", "")
            password = data.get("password", "")
            if username == "":
                self.send_json(200, {"code": 1001, "message": "username required"})
            elif password == "":
                self.send_json(200, {"code": 1002, "message": "password required"})
            elif username in USERS and USERS[username]["password"] == password:
                token = f"token_{username}_12345"
                TOKEN_STORE[token] = username
                self.send_json(200, {"code": 0, "message": "success", "token": token})
            else:
                self.send_json(200, {"code": 1003, "message": "username or password error"})
        else:
            self.send_json(404, {"code": 404, "message": "接口不存在"})

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), APIHandler)
    print("Day 3 服务已启动：http://127.0.0.1:5000")
    print("按 Ctrl + C 停止")
    server.serve_forever()