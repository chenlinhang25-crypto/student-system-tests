from itertools import count

import pytest
import requests
import allure

from day1_python_practice import result


@allure.feature("学生管理系统")
class TestStudentSystem:

    @allure.story("添加学生")
    @pytest.mark.parametrize("case", [
        {"id": "8001", "name": "张三"},
        {"id": "8002", "name": "李四"},
        {"id": "8003", "name": "王五"},
    ])
    def test_add_student(self, case, base_url):
        with allure.step(f"添加学生: {case['name']}"):
            response = requests.post(
                f"{base_url}/student",
                json=case
            )
            result = response.json()
            assert result["code"] == 0
            allure.attach(f"学生ID: {case['id']}", "请求参数")

    # 你来写：测试录入成绩
    def test_add_score(self, new_student, base_url):
        response = requests.post(
            url=f"{base_url}/score",
            json={"student_id": new_student, "subject": "数学", "score": 90},
        )
        assert response.json()["code"] == 0

    # 你来写：测试查询成绩
    def test_get_score(self, new_student, base_url):
        response1 = requests.get(
            url=f"{base_url}/score/{new_student}",
        )
        result = response1.json()
        assert result["code"] == 0
        assert "数学" in result["data"]

    # 你来写：测试计算平均分
    def test_get_average(self, new_student, base_url):
        student_id = new_student
        response = requests.get(
            url=f"{base_url}/average/{student_id}",
        )
        result = response.json()
        assert result["code"] == 0
        assert result["data"]["count"] >=1
        assert isinstance(result["data"]["average"], (int, float))