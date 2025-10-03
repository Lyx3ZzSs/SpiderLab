"""
@Author: yuanxin.Li
@Time：2025/10/3 14:51
@Version: 1.0
@Description:
"""
import requests

url = "https://www.baidu.com/"
response = requests.get(url)

print(response.content)

# 打印响应对应请求的请求头信息
print(response.request.headers)
