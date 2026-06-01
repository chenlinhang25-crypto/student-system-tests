import requests

url = "http://127.0.0.1:5000/login"

response = requests.get(url)

print("状态码：", response.status_code)
print("返回内容：", response.json())