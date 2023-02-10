"""
编写代码，计算从1到100中偶数的数字和
即：2+4+6+8+.....+98+100

效果如下
2550
"""
# 方法一、使用切片和步长进行处理
# numbers = list(range(1,101))[1::2]
# print(sum(numbers))
# 方法二、使用循环和判断进行处理
sum_result = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    else:
        sum_result += i
print(sum_result)
