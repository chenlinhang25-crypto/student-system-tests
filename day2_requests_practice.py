"""
Day 2: requests 接口测试练习

运行方式：
cd "C:/Users/陈林航/Documents/Codex/2026-05-28/new-chat"
python ./day2_requests_practice.py

今天目标：
1. 用 requests.post 真的请求登录接口
2. 看懂 response.status_code
3. 看懂 response.json()
4. 判断接口返回的业务 code 是否符合预期
"""

import requests


url = "http://127.0.0.1:5000/login"


print("========== 1. 发送一次正确登录请求 ==========")

response = requests.post(
    url,
    json={
        "username": "admin",
        "password": "123456",
    },
)

print("HTTP 状态码：", response.status_code)
print("接口返回 JSON：", response.json())


print("\n========== 2. 取出响应里的字段 ==========")

actual_result = response.json()

print("业务 code：", actual_result["code"])
print("提示信息：", actual_result["message"])
print("token：", actual_result["token"])


print("\n========== 3. 判断是否登录成功 ==========")

if actual_result["code"] == 0 and actual_result["token"] != "":
    print("通过：登录成功，并且返回了 token")
else:
    print("失败：登录结果不符合预期")


print("\n========== 4. 批量测试多个登录场景 ==========")

test_cases = [
    {"case_name": "正确用户名和密码", "username": "admin", "password": "123456", "expected_code": 0},
    {"case_name": "用户名为空", "username": "", "password": "123456", "expected_code": 1001},
    {"case_name": "密码为空", "username": "admin", "password": "", "expected_code": 1002},
    {"case_name": "密码错误", "username": "admin", "password": "wrong", "expected_code": 1003},
    {"case_name": "用户名错误", "username": "test", "password": "123456", "expected_code": 1003},
]

for case in test_cases:
    response = requests.post(
        url,
        json={
            "username": case["username"],
            "password": case["password"],
        },
    )
    actual_result = response.json()
    actual_code = actual_result["code"]
    expected_code = case["expected_code"]

    if actual_code == expected_code:
        print("通过：", case["case_name"])
    else:
        print("失败：", case["case_name"])
        print("期望 code：", expected_code)
        print("实际 code：", actual_code)


print("\n========== 今日小作业 ==========")
print("请你新增一条用例：用户名错误")
print('{"case_name": "用户名错误", "username": "test", "password": "123456", "expected_code": 1003}')
print("加到 test_cases 里，然后重新运行。")

