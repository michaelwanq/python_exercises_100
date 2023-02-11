"""
完成如下步骤：
用python加载p060.json文件，转成字典
给 employees 添加一个人：
'firstName': 'Albert', 'lastName': 'Bert'
将数据生成json，结果存到 p062.json文件
"""
import json

with open("p060.json") as f:
    d = json.loads(f.read())

d["employees"].append({'firstName': 'Albert', 'lastName': 'Bert'})

with open("p062.json", "w") as f:
    f.write(json.dumps(d, indent=2))
