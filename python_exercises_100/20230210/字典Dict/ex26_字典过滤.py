"""
移除如下字典中所有value大于1的key:value对
d = {"a": 1, "b": 2, "c": 3}
过滤后，产生如下输出
{'a': 1}
"""
# 方法一、使用推导式
# d = {"a": 1, "b": 2, "c": 3}
# d = {key: value for key, value in d.items() if value <= 1}
# print(d)
# 方法二、使用循环处理
del_d = {}
d = {"a": 1, "b": 2, "c": 3}
for k,v in d.items():
    if v > 1:
        continue
    else:
        del_d[k] = v

print(del_d)