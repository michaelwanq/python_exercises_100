"""
如下代码会报错，你知道为什么吗？怎么修复？
age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
"""
age = input("What's your age? ")
age_last_year = int(age) - 1 # input函数获取的用户输入类型为字符串类型
print("Last year you were %s." % age_last_year)
