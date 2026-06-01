import pytest
import requests
import allure  # 导入 allure

test_data = [
    {"id": "7001", "name": "张三"},
    {"id": "7002", "name": "张s"},
    {"id": "7003", "name": "张2"},
]


@allure.feature("学生管理")  # Allure：功能模块
@allure.story("添加学生")  # Allure：用户故事
class TestParametrize:

    @pytest.mark.parametrize("case", test_data)
    def test_add_student(self, case, base_url):
        # Allure：测试步骤
        with allure.step(f"添加学生: {case['name']}"):
            response = requests.post(
                f"{base_url}/student",
                json={"id": case["id"], "name": case["name"]}
            )
            result = response.json()

        # Allure：断言
        with allure.step("验证返回结果"):
            assert result["code"] == 0
            allure.attach(f"学生ID: {case['id']}", "请求参数")  # 附加信息

        print(f"添加成功: {case['name']}")