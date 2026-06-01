
import pytest
import requests

url = "http://127.0.0.1:5000/login"

test_cases = [
    {"case_name": "正确用户名和密码", "username": "admin", "password": "123456", "expected_code": 0},
    {"case_name": "用户名为空", "username": "", "password": "123456", "expected_code": 1001},
    {"case_name": "密码为空", "username": "admin", "password": "", "expected_code": 1002},
    {"case_name": "密码错误", "username": "admin", "password": "wrong", "expected_code": 1003},
]


@pytest.mark.parametrize("case", test_cases, ids=[case["case_name"] for case in test_cases])
def test_login_code(case):
    response = requests.post(
        url,
        json={
            "username": case["username"],
            "password": case["password"],
        }
    )
    actual_result = response.json()
    actual_code = actual_result["code"]
    expected_code = case["expected_code"]
    assert actual_code == expected_code


def test_login_success_has_token():
    response = requests.post(
        url,
        json={
            "username": "admin",
            "password": "123456",
        }
    )
    actual_result = response.json()

    assert actual_result["code"] == 0
    assert "token" in actual_result
    assert actual_result["token"] != ""
