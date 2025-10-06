"""
@Author: yuanxin.Li
@Time：2025/10/6 17:36
@Version: 1.0
@Description:
"""
import requests

post_url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

response = requests.post(url=post_url, headers=headers, json={"kw": "python"}, timeout=3)
print("请求头是：", response.request.headers)
print("请求体是：", response.request.body)
