"""
编写Python代码，需要用户一直输入密码，直到满足如下条件才退出循环：
至少包含一个数字；
至少包含一个大写字母；
密码至少6位数；
"""
import string
while True:
    password = input("请输入你的用户密码：")
    len = len(password)
    if string.ascii_lowercase in password and string.ascii_uppercase in password and len >=6:
        print(f'你输入的密码是：{password}，已生效！')
    else:
        print('你输入的密码不符合要求，请重新输入！')