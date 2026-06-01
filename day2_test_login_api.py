"""
Day 2 pytest version: real login API test (refactored).

Run:
cd "C:/Users/陈林航/Documents/Codex/2026-05-28/new-chat"
D:/Python/Python310/python.exe -m pytest ./day2_test_login_api.py -v
"""

import pytest
import requests


URL = "http://127.0.0.1:5000/login"


def login(username: str, password: str):
    """封装登录请求，方便复用"""
    response = requests.post(
        URL,
        json={"username": username, "password": password},
        timeout=5,  # 加超时，防止卡死
    )
    return response


test_cases = [
    {
        "case_name": "success_login",
        "username": "admin",
        "password": "123456",
        "expected_code": 0,
        "expected_message": "success",
        "check_token": True,  # 标记需要校验token
    },
    {
        "case_name": "empty_username",
        "username": "",
        "password": "123456",
        "expected_code": 1001,
        "expected_message": "username required",
        "check_token": False,
    },
    {
        "case_name": "empty_password",
        "username": "admin",
        "password": "",
        "expected_code": 1002,
        "expected_message": "password required",
        "check_token": False,
    },
    {
        "case_name": "wrong_password",
        "username": "admin",
        "password": "wrong",
        "expected_code": 1003,
        "expected_message": "username or password error",
        "check_token": False,
    },
    {
        "case_name": "wrong_username",
        "username": "test",
        "password": "123456",
        "expected_code": 1003,
        "expected_message": "username or password error",
        "check_token": False,
    },
]


@pytest.mark.parametrize("case", test_cases, ids=[case["case_name"] for case in test_cases])
def test_login(case):
    """统一的登录测试函数"""
    # 发送请求
    response = login(case["username"], case["password"])
    actual = response.json()

    # 基础断言（带自定义失败信息）
    assert response.status_code == 200, f"HTTP状态码错误，实际: {response.status_code}"
    assert actual["code"] == case["expected_code"], \
        f"业务code错误，期望: {case['expected_code']}, 实际: {actual['code']}"
    assert actual["message"] == case["expected_message"], \
        f"message错误，期望: '{case['expected_message']}', 实际: '{actual['message']}'"

    # token校验（仅登录成功时）
    if case.get("check_token"):
        assert "token" in actual, "响应中缺少token字段"
        assert actual["token"] != "", "token为空字符串"
        assert isinstance(actual["token"], str), "token类型不是字符串"
        print(f"\n[调试] 获取到token: {actual['token'][:10]}...")  # 只打印前10位


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "-s"]))  # -s 允许print输出