"""
编写Python代码，用户可以输入年龄数字，程序打印生日年份
请输入年龄：20
你的出生年份是：2002
"""
from datetime import datetime

age = input('请输入你的年龄：')
year_birth = datetime.now().year - int(age)
print(f"你的出生年份是：{year_birth}")
