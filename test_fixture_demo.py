"""
Day 4: 使用 conftest.py 中的 fixture
"""
import pytest
import requests

from day1_python_practice import response


class TestWithConftest:
    """这些测试直接用 conftest.py 里的 fixture"""


    def test_add_score(self, new_student, base_url):
        """用 conftest 的 new_student 和 base_url"""
        print(f"\n[test] base_url = {base_url}")
        print(f"[test] 学生ID = {new_student}")

        response = requests.post(
            f"{base_url}/score",
            json={"student_id": new_student, "subject": "英语", "score": 88}
        )
        result = response.json()
        assert result["code"] == 0
        print(f"[test] 添加成绩: {result}")

    def test_get_score(self, new_student, base_url):
        """另一个测试也用 conftest 的 fixture"""
        response = requests.get(f"{base_url}/score/{new_student}")
        result = response.json()
        print(f"\n[test] 查询结果: {result}")
        assert result["code"] == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])




