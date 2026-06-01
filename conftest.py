"""
conftest.py - 共享 fixture
同目录下所有测试文件自动可用，不需要 import
"""

import pytest
import requests

BASE_URL = "http://127.0.0.1:5001"


@pytest.fixture(scope="function")
def new_student():
    """创建新学生（所有测试文件都能用）"""
    student_id = "conftest_001"
    print(f"\n[conftest] 创建学生: {student_id}")
    requests.post(
        f"{BASE_URL}/student",
        json={"id": student_id, "name": "conftest学生"}
    )
    yield student_id
    print(f"[conftest] 测试结束: {student_id}")


@pytest.fixture(scope="session")
def base_url():
    """提供基础 URL"""
    return BASE_URL