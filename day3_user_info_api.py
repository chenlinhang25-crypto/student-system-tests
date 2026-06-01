"""
Day 3: 接口关联测试
"""

import pytest
import requests

LOGIN_URL = "http://127.0.0.1:5000/login"
USER_INFO_URL = "http://127.0.0.1:5000/user_info"

def test_login_and_get_user_info():
    """接口关联：登录 → 获取 token → 用 token 获取用户信息"""
    print("\n[第一步] 正在登录...")
    response = requests.post(LOGIN_URL, json={"username": "admin", "password": "123456"}, timeout=5)
    result = response.json()
    assert result["code"] == 0, f"登录失败: {result}"
    assert "token" in result, "没拿到 token"
    token = result["token"]
    print(f"[成功] token = {token}")

    print("\n[第二步] 获取用户信息...")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(USER_INFO_URL, headers=headers, timeout=5)
    result = response.json()
    assert result["code"] == 0, f"获取失败: {result}"
    assert result["data"]["username"] == "admin"
    print(f"[成功] 用户信息: {result['data']}")

def test_user_info_without_token():
    """不带 token 应该被拒绝"""
    response = requests.get(USER_INFO_URL, timeout=5)
    result = response.json()
    assert response.status_code == 401
    assert result["code"] == 401
    print(f"[预期] 被拒绝: {result['message']}")

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v", "-s"]))