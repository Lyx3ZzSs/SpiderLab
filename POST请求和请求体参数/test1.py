"""
@Author: yuanxin.Li
@Time：2025/10/5 23:39
@Version: 1.0
@Description:
"""
import requests
import json

url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
data = {
    "kw": "java"
}

response = requests.post(url=url, headers=headers, data=data)
dict_obj = response.json()
print(dict_obj)

fp = open('./baidu.json', 'w', encoding='utf-8')
json.dump(dict_obj, fp=fp, ensure_ascii=False)
print('数据爬取结束！')
