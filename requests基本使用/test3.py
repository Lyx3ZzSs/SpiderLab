"""
@Author: yuanxin.Li
@Time：2025/10/3 14:30
@Version: 1.0
@Description:
"""
import requests

# 目标url
url = "https://www.baidu.com/"

# 发送GET请求
response = requests.get(url)

try:
    content = response.content.decode()
except UnicodeDecodeError:
    try:
        content = response.content.decode('GBK')
    except UnicodeDecodeError:
        content = response.text

# 打印解码后的内容
print(content)