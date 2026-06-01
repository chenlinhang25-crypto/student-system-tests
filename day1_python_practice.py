"""
Day 1: Python 脚本基础练习

运行方式：
1. 打开 PowerShell
2. 进入目录：
   cd "C:/Users/陈林航/Documents/Codex/2026-05-28/new-chat"
3. 运行：
   python ./day1_python_practice.py

你可以先直接运行，再改里面的数据看看输出怎么变。
"""


print("========== 1. 变量 ==========")

case_name = "登录接口"
status_code = 200
is_success = True

print("用例名称：", case_name)
print("状态码：", status_code)
print("是否成功：", is_success)


print("\n========== 2. 字典：像接口响应 JSON ==========")

response = {
    "code": 0,
    "message": "success",
    "data": {
        "username": "admin",
        "token": "abc123"
    }
}

print("完整响应：", response)
print("业务 code：", response["code"])
print("用户名：", response["data"]["username"])
print("token：", response["data"]["token"])


print("\n========== 3. 列表：多条测试用例 ==========")

test_cases = [
    {"username": "admin", "password": "123456", "expected_code": 0},
    {"username": "", "password": "123456", "expected_code": 1001},
    {"username": "admin", "password": "", "expected_code": 1002},
{"username": "admin", "password": "wrong", "expected_code": 1003},
]

for case in test_cases:

    print("正在测试：", case)


print("\n========== 4. 函数：封装重复逻辑 ==========")


def fake_login(username, password):
    """模拟一个登录接口，不是真的请求网络。"""
    if username == "":
        return {"code": 1001, "message": "username required"}
    if password == "":
        return {"code": 1002, "message": "password required"}
    if username == "admin" and password == "123456":
        return {"code": 0, "message": "success", "token": "abc123"}
    return {"code": 1003, "message": "username or password error"}


result = fake_login("admin", "123456")
print("登录结果：", result)


print("\n========== 5. 断言：自动判断是否通过 ==========")

for case in test_cases:
    actual_result = fake_login(case["username"], case["password"])
    actual_code = actual_result["code"]
    expected_code = case["expected_code"]

    if actual_code == expected_code:
        print("通过：", case)
    else:
        print("失败：", case)
        print("期望 code：", expected_code)
        print("实际 code：", actual_code)


print("\n========== 6. 异常处理：避免脚本直接崩掉 ==========")

user = {"name": "Alice"}

try:
    print(user["age"])
except KeyError:
    print("字典里没有 age 字段，所以这里捕获了 KeyError")


print("\n========== 7. 一个小作业 ==========")
print("请你修改 test_cases，新增一条错误密码的用例：")
print('{"username": "admin", "password": "wrong", "expected_code": 1003}')
print("然后重新运行，看它是否通过。")
