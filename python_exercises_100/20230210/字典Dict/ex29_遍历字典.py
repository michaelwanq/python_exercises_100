"""
遍历如下字典:
d = {"a": list(range(1, 11)),
     "b": list(range(11, 21)),
     "c": list(range(21, 31))}
得到如下三行输出
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
"""
d = {"a": list(range(1, 11)),
     "b": list(range(11, 21)),
     "c": list(range(21, 31))
     }
for k,v in d.items():
    print(f'{k} has value {v}')