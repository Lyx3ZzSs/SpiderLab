"""
@Author: yuanxin.Li
@Time：2025/10/3 14:37
@Version: 1.0
@Description:
"""
import requests

url = "https://www.baidu.com/"

response = requests.get(url=url)

print("---状态码如下---")
print(response.status_code)

print("---响应对应的请求头---")
print(response.request.headers)

print("---响应头---")
print(response.headers)

print("---bytes类型数据---")
print(response.content)

print("---str类型数据---")
print(response.text)

print("---str类型数据（utf-8)---")
print(response.content.decode("utf-8"))
