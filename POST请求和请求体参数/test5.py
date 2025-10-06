"""
@Author: yuanxin.Li
@Time：2025/10/6 20:54
@Version: 1.0
@Description:
"""
import requests

post_url = "https://www.d21d965.top/user/bookcase.html"

# 创建一个可以自动传递cookie的Session对象
session = requests.session()

data = {
    "username": "13051658038",
    "password": "Lyx19971228"
}

headers = {
    "Referer": "https://www.e00df.icu/user/login.html",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.post(url=post_url, data=data, headers=headers)

print(response.text)

# 持久化存储
with open("./bookcase.html", "w", encoding="utf-8") as fp:
    fp.write(response.text)
    print("保存成功")
