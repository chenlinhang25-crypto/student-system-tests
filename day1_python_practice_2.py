"""
Day 1 进阶练习：生成简单测试报告

运行方式：
cd "C:/Users/陈林航/Documents/Codex/2026-05-28/new-chat"
python ./day1_python_practice_2.py

目标：
1. 继续使用测试数据 test_cases
2. 调用 fake_login 模拟接口
3. 自动判断通过/失败
4. 统计通过数量、失败数量
5. 生成 test_report.txt
"""


def fake_login(username, password):
    if username == "":
        return {"code": 1001, "message": "username required"}
    if password == "":
        return {"code": 1002, "message": "password required"}
    if username == "admin" and password == "123456":
        return {"code": 0, "message": "success", "token": "abc123"}
    return {"code": 1003, "message": "username or password error"}


test_cases = [
    {"case_name": "正确用户名和密码", "username": "admin", "password": "123456", "expected_code": 0},
    {"case_name": "用户名为空", "username": "", "password": "123456", "expected_code": 1001},
    {"case_name": "密码为空", "username": "admin", "password": "", "expected_code": 1002},
    {"case_name": "密码错误", "username": "admin", "password": "wrong", "expected_code": 0},
]

passed_count = 0
failed_count = 0
report_lines = []

print("========== 开始执行登录接口测试 ==========")

for case in test_cases:
    actual_result = fake_login(case["username"], case["password"])
    actual_code = actual_result["code"]
    expected_code = case["expected_code"]

    if actual_code == expected_code:
        passed_count = passed_count + 1
        line = f"通过 | {case['case_name']} | 期望: {expected_code} | 实际: {actual_code}"
    else:
        failed_count = failed_count + 1
        line = f"失败 | {case['case_name']} | 期望: {expected_code} | 实际: {actual_code}"

    print(line)
    report_lines.append(line)

summary = f"总用例数: {len(test_cases)}，通过: {passed_count}，失败: {failed_count}"
print("========== 测试汇总 ==========")
print(summary)

with open("test_report.txt", "w", encoding="utf-8") as file:
    file.write("登录接口测试报告\n")
    file.write("================\n")
    for line in report_lines:
        file.write(line + "\n")
    file.write("================\n")
    file.write(summary + "\n")

print("测试报告已生成：test_report.txt")

