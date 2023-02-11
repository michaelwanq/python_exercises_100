"""
JSON变字典
用python加载p60.json文件，转成字典，并且进行格式化输出
"""
import json
import pprint

with open('p060.txt') as f:
    pprint.pprint(json.loads(f.read()))
