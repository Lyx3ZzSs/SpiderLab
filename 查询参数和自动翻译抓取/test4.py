"""
@Author: yuanxin.Li
@Time：2025/10/5 23:18
@Version: 1.0
@Description:
"""
import requests
import json

url = "https://movie.douban.com/j/chart/top_list"

params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.get(url=url, params=params, headers=headers)
list_data = response.json()
fp = open("./douban.json", "w", encoding="utf-8")
json.dump(list_data, fp=fp, ensure_ascii=False)
print("保存成功")
