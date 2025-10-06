"""
@Author: yuanxin.Li
@Time：2025/10/6 17:15
@Version: 1.0
@Description:
"""
import json
import requests
import time

post_url = "https://fanyi.baidu.com/sug"

# 进行UA伪装(尽量使用最新浏览器的真是User-Agent）
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Referer": "https://fanyi.baidu.com/mtpe-individual/transText",
    # 添加Cookie字段（从浏览器复制）
    "Cookie": "BIDUPSID=8C0AAA502FE4D50B7347D4725CAE87BB; PSTM=1730189477; newlogin=1; BDUSS=ZLeTZjMmR1OW5mSlRCVE5YbWRGcjlrSnV4UFloSDBOUnd2LWE5c1h6aURmcDFuRUFBQUFBJCQAAAAAABAAAAEAAACToxT7THl4M1p6U3MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIPxdWeD8XVnaV; BDUSS_BFESS=ZLeTZjMmR1OW5mSlRCVE5YbWRGcjlrSnV4UFloSDBOUnd2LWE5c1h6aURmcDFuRUFBQUFBJCQAAAAAABAAAAEAAACToxT7THl4M1p6U3MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIPxdWeD8XVnaV; MCITY=-%3A; BAIDUID=102FFBAA6D94DE3B7067D0FD0567FE98:FG=1; BAIDUID_BFESS=102FFBAA6D94DE3B7067D0FD0567FE98:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; BA_HECTOR=alal0h8m85018la181048k8hag94a61ke4vk425; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=60273_63141_64752_64870_64972_65130_65192_65220_65251_65258_65273_65367_65423_65455_65451_65488_65503_65475_65508_65538_65542; ZFY=H0B9iBy8JzzPZ:AMubdmcgzTaWDPD:A69jiUXnTLagImE:C; H_PS_PSSID=60273_63141_64752_64870_64972_65130_65192_65220_65251_65258_65273_65367_65423_65455_65451_65488_65503_65527_65475_65508_65538_65542; AIT_PERSONAL_VERSION=1; AIT_ENTERPRISE_VERSION=1; ab_sr=1.0.1_NWRkMjc1ZGQyMzcyODM0YTE0YmI0ZDdmYTlhZTk4YmYyYjE3MTg0YmQ4NzcxZDk3ODk4ZjFiOGQ2YzFiM2U1OTMyYjcyMzZmNDNjYWM1N2I5MTM3ZWVjOTAwYjc3NzA1MjY4ZGE4OWU2ZmY3YTBkODdlNzZkYTBmMWQ4YThmNGYwMzUyNmQyM2UwODRkOWYxOGM1NTViM2I1NWE1NTQ5Yg==; RT=\"z=1&dm=baidu.com&si=0f18427b-4709-406b-9e90-50e557279f00&ss=mgex2ytr&sl=4&tt=5n2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=18zt\""
}

# 3.POST请求参数处理
data = {
    "kw": "java"
}

response = requests.post(url=post_url, headers=headers, data=data)
try:
    dict_obj = response.json()
    print(dict_obj)
except requests.exceptions.JSONDecodeError:
    print("响应内容不是合法的 JSON 格式，请检查返回内容：", response.text)

with open("./baidu.json", "w", encoding="utf-8") as fp:
    json.dump(dict_obj, fp, ensure_ascii=False)
print("爬取结束")
