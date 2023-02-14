"""
编写Python代码，需要用户一直输入密码，直到满足如下条件才退出循环：
至少包含一个数字；
至少包含一个大写字母；
密码至少6位数；
"""
# import string
# while True:
#     password = input("请输入你的用户密码：")
#     word = str(password)
#     if len(word) >=6:
#         for i in string.ascii_lowercase:
#             if i in word:
#                 print(f'你输入的密码是：{word}，已生效！')
#
#     else:
#         print('你输入的密码不符合要求，请重新输入！')
while True:
    pwd = input("请输入密码: ")
    have_number = any([i.isdigit() for i in pwd])
    have_upper = any([i.isupper() for i in pwd])

    if have_number and have_upper and len(pwd) >= 6:
        print("密码校验通过")
        break
    else:
        print("密码校验不通过，请重新输入")
