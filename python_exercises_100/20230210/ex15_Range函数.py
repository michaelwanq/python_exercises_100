# 编写代码，生成如下数字List，注意要用函数生成，别手动生成
"""
方法一、列表加循环
numbers = []
for i in range(1,21):
    numbers.append(i)
print(numbers)
"""
# 方法二
numbers = range(1,21)
print(list(numbers))