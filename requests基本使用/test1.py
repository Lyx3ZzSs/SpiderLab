"""
@Author: yuanxin.Li
@Time：2025/10/3 14:22
@Version: 1.0
@Description:
"""
import requests

# 目标url
url = "https://www.baidu.com/"

# 向目标url发送GET请求
response = requests.get(url)

# 打印响应内容
print(response.text)
