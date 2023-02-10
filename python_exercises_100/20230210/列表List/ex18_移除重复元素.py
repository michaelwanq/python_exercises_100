"""
完成代码，移除列表中的重复值
a = ["1", 1, "1", 2]
最终产生如下输出：
['1', 2, 1]
"""
# 方法一、
# numbers = []
# a = ["1", 1, "1", 2]
# for number in a:
#     if number in numbers:
#         continue
#     else:
#         numbers.append(number)
# print(numbers)
# 方法二、使用集合去重
a = ["1", 1, "1", 2]
print(list(set(a)))
