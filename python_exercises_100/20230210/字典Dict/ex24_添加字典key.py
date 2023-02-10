"""
给如下代码新增一对key:value，key是c，value是3
d = {"a": 1, "b": 2}
最终产生如下输出
{'a': 1, 'c': 3, 'b': 2}
"""
d = {"a": 1, "b": 2}
d['c'] = 3
print(d)