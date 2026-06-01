
import pytest
import requests



BASE_URL = "http://192.168.31.117:5001"  # 你的服务器地址

# 1. base_url fixture
@pytest.fixture
def base_url():
    return BASE_URL

# 2. new_student fixture（创建学生，返回ID）
@pytest.fixture
def new_student(base_url):
    student_id = "test_001"
    response = requests.post(f'{base_url}/student', json={"id": student_id,"name":"xues"})
    assert response.json()["code"] == 0
    yield student_id
    print(f"测试结束，学生{student_id}")