"""
完成如下代码:
my_range = range(1, 21)
你的代码需要使用my_range变量完成，最终产生如下输出：
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
"""
# 方法一、列表和循环
# numbers = []
# my_range = range(1, 21)
# for i in range(1,21):
#     i = i * 10
#     numbers.append(i)
# print(numbers)
# 方法二、使用推导式
my_range = range(1, 21)
# 列表推导式用于快速生成一个列表，形如：[x*2 for x in list if x>3]。
print([x * 10 for x in my_range])

