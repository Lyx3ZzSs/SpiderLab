"""
@Author: yuanxin.Li
@Time：2025/10/6 17:41
@Version: 1.0
@Description:
"""
import json

info = {
    "name": "张三",
    "skill": None,
    "spider": False,
    "money": 100000000000,
    "is": True,
    "addr": "567uiaaaa",
    "li": [111, 222, 343]
}

# 方法1：json.dumps()   将python的数据格式 转换为 json串
res = json.dumps(info, ensure_ascii=False)
print(res, type(res))


# 方法2：json.loads()   将json串 转换为 python的数据格式
ss = '{"name": "张三", "skill": null, "spider": false, "money": 100000000000, "is": true, "addr": "567uiaaaa", "li": [111, 222, 343]}'

res2 = json.loads(ss)
print(ss)
print(res2)
