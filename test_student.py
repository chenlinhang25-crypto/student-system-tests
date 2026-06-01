"""
学生成绩管理系统 - Bug 测试
找到 5 个 Bug 并验证
"""

import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"


class TestBug1:
    """Bug 1: 重复添加学生不报错"""

    def test_add_duplicate_student(self):
        # 先添加一次
        response1 = requests.post(
            f"{BASE_URL}/student",
            json={"id": "1001", "name": "张三"}
        )
        assert response1.json()["code"] == 0

        # 再添加同一个 ID（不同名字）
        response2 = requests.post(
            f"{BASE_URL}/student",
            json={"id": "1001", "name": "李四"}
        )
        result = response2.json()

        print(f"\n[Bug 1] 重复添加结果: {result}")

        # Bug: 应该返回错误码，实际返回成功
        # 正确做法: assert result["code"] != 0
        # Bug 现象: assert result["code"] == 0  # 居然成功了！


class TestBug2:
    """Bug 2: 查询不存在学生，HTTP 状态码返回 200"""

    def test_get_nonexistent_student(self):
        response = requests.get(f"{BASE_URL}/student/9999")

        print(f"\n[Bug 2] HTTP 状态码: {response.status_code}")
        print(f"[Bug 2] 响应内容: {response.json()}")

        # Bug: HTTP 状态码应该是 404，实际是 200
        # 正确做法: assert response.status_code == 404
        # Bug 现象: assert response.status_code == 200  # 错误！


class TestBug3:
    """Bug 3: 分数超过 100 也能录入"""

    def test_add_score_over_100(self):
        # 添加学生
        requests.post(f"{BASE_URL}/student", json={"id": "2001", "name": "测试学生"})

        # 录入超过 100 的分数
        response = requests.post(
            f"{BASE_URL}/score",
            json={"student_id": "2001", "subject": "数学", "score": 150}
        )
        result = response.json()

        print(f"\n[Bug 3] 分数 150 录入结果: {result}")

        # Bug: 应该返回错误，实际返回成功
        # 正确做法: assert result["code"] != 0
        # Bug 现象: assert result["code"] == 0  # 居然成功了！


class TestBug4:
    """Bug 4: 无成绩算平均分报 500"""

    def test_average_no_scores(self):
        # 添加学生但不录入成绩
        requests.post(f"{BASE_URL}/student", json={"id": "3001", "name": "无成绩学生"})

        # 计算平均分
        response = requests.get(f"{BASE_URL}/average/3001")

        print(f"\n[Bug 4] HTTP 状态码: {response.status_code}")
        print(f"[Bug 4] 响应内容: {response.text}")

        # Bug: 应该返回提示信息，实际报 500 错误
        assert response.status_code == 500  # 服务器内部错误！


class TestBug5:
    """Bug 5: 查询无成绩学生返回空对象，无提示"""

    def test_get_scores_empty(self):
        # 添加学生但不录入成绩
        requests.post(f"{BASE_URL}/student", json={"id": "4001", "name": "无成绩学生"})

        # 查询成绩
        response = requests.get(f"{BASE_URL}/score/4001")
        result = response.json()

        print(f"\n[Bug 5] 无成绩查询结果: {result}")

        # Bug: 应该有提示信息，实际返回空对象
        assert result["code"] == 0
        assert result["data"] == {}  # 空对象，没有提示！


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])