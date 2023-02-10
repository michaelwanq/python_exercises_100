"""
计算如下字典的所有value的数字的和
d = {"a": 1, "b": 2, "c": 3}
最终产生如下输出
6
"""
d = {"a": 1, "b": 2, "c": 3}
# 方法一、使用循环取出所有value值，进行加总
# for values in d.values():
#     values += values
#
# print(values)
# 方法二、直接使用sum函数，对d.values()的列表值进行加总操作
print(sum(d.values()))