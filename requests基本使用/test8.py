"""
@Author: yuanxin.Li
@Time：2025/10/3 15:17
@Version: 1.0
@Description:
"""
import requests

url = "https://www.baidu.com/img/bd_logo1.png"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

with open("baidu.png", "wb") as f:
    f.write(response.content)

print("爬取结束")
