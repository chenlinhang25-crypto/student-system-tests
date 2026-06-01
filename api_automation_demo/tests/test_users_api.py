import allure
import pytest
import requests

from utils.data_loader import load_yaml


cases = load_yaml("data/cases.yaml")


@allure.feature("用户接口")
@pytest.mark.parametrize("case", cases, ids=[case["name"] for case in cases])
def test_users_api(base_url, case):
    url = base_url + case["path"]

    with allure.step(f"请求接口：{case['method']} {case['path']}"):
        response = requests.request(
            method=case["method"],
            url=url,
            json=case.get("json"),
            timeout=5,
        )

    with allure.step("校验状态码"):
        assert response.status_code == case["expected_status"]

    body = response.json()
    if "expected_name" in case:
        with allure.step("校验用户名称"):
            assert body["name"] == case["expected_name"]
    if "expected_error" in case:
        with allure.step("校验错误信息"):
            assert body["error"] == case["expected_error"]
