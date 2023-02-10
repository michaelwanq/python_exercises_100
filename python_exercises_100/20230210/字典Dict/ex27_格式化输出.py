"""
创建一个字典
key是a、b、c，value分别是列表1~10、列表11~20、列表21~30
格式化输出字典
最终产生如下输出：
{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
"""
from pprint import pprint

d = {"a": list(range(1, 11)),
     "b": list(range(11, 21)),
     "c": list(range(21, 31))}

# 方法一、导入pprint模块，使用pprint函数进行字典打印
# pprint(d)
# 方法二、使用print格式化输出方式进行循环打印
for k,v in d.items():
    k = f'\'{k}\''
    print(k + ': ' + str(v))
