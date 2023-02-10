"""
对于如下字典:
d = {"a": list(range(1, 11)),
     "b": list(range(11, 21)),
     "c": list(range(21, 31))}
怎样访问key=b的列表的第3个元素，输出如下数字
13
"""
d = {"a": list(range(1, 11)),
     "b": list(range(11, 21)),
     "c": list(range(21, 31))
     }
print(d['b'][2])

