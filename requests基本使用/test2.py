"""
@Author: yuanxin.Li
@Time：2025/10/3 14:26
@Version: 1.0
@Description:
"""
import requests

r = requests.get("https://www.baidu.com/")

print("-----requests一般能够根据响应自动解码-----")
print(r.text)

print("-----如果不能够解析出想要的真实数据，可以通过设置解码方式-----")
r.encoding = "utf-8"
print(r.text)
