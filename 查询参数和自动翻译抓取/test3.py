"""
@Author: yuanxin.Li
@Time：2025/10/5 22:43
@Version: 1.0
@Description:
"""
import requests

# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
url = "https://so.toutiao.com/search"

ip = input("指定搜索关键字：")
param = {
    "keyword": ip
}

response = requests.get(url=url, headers=headers, params=param)
response.encoding = "utf-8"
# 3.获取响应数据
res_text = response.text

fileName = ip + '.html'

# 4.持久化存储
with open(fileName, 'w', encoding='utf-8') as f:
    f.write(res_text)
print(fileName, '保存成功！！！')
