import pytest
import requests
import allure

test_data = [
    {"id": "7001", "name": "张三"},
    {"id": "7002", "name": "张s"},
    {"id": "7003", "name": "张2"},
]

BASE_URL = "http://192.168.31.117:5001"


@allure.feature("学生管理")
@allure.story("添加学生")
class TestParametrize:

    @pytest.mark.parametrize("case", test_data)
    def test_add_student(self, case):
        with allure.step(f"添加学生: {case['name']}"):
            response = requests.post(
                f"{BASE_URL}/student",
                json={"id": case["id"], "name": case["name"]}
            )
            result = response.json()

        with allure.step("验证返回结果"):
            assert result["code"] == 0
            allure.attach(f"学生ID: {case['id']}", "请求参数")

        print(f"添加成功: {case['name']}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--alluredir=./allure-results"])