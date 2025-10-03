"""
@Author: yuanxin.Li
@Time：2025/10/3 14:59
@Version: 1.0
@Description:
"""
import requests

url = "https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

# 获取页面源码
print(response.content.decode())
