"""
编写代码，计算从1到100的和，包含1和100
即：1+2+3+4+.....+99+100

效果如下:
5050
"""
# 方法一、使用list将range列表话，然后使用sum函数对列表元素求和
# sum_result = sum(list(range(1,101)))
# print(sum_result)
# 方法二、使用循环对range对象内的元素加总求和
sum_result = 0
for i in range(1, 101):
    sum_result += i
print(sum_result)
