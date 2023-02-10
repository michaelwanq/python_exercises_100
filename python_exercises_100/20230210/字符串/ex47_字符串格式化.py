"""
如下代码让用户输入name和age，然后拼接字符串
但是代码会报错 TypeError
你知道为什么吗？怎么修复？有另一种办法吗？
name = input("Enter name: ")
age = input("Enter age: ")
print("Your name is %s and your age is %s" % name, age)
"""
# 方法一
# name = input("Enter name: ")
# age = input("Enter age: ")
# print("Your name is %s and your age is %s" % (name, age))
# 格式化字符串输出时的格式不对
# 方法二
name = input("Enter name: ")
age = input("Enter age: ")
print("Your name is %s and your age is %s" % name, age)