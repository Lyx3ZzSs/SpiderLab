"""
@Author: yuanxin.Li
@Time：2025/10/3 15:08
@Version: 1.0
@Description:
"""
import requests

url = "https://www.baidu.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.content.decode())

with open("./baidu.html", "w", encoding="utf-8") as f:
    f.write(response.text)
print("爬取数据结束！！！")
