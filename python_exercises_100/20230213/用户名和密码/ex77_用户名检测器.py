"""
编写Python代码，要求用户输入用户名，进行检测：
1、用户名至少6位；
2、文件名不能在文件p077_users.txt中存在
自己新建文件：p077_users.txt，粘贴如下内容进去：
xiaoming
xiaowang
xiaozhang
xiaozhao
xiaoqian
xiaosun
"""
# 方法一
# def user_check(username):
#     with open('p077_users.txt') as f:
#                 user_list = f.read()
#                 if len(username) < 6:
#                     print('用户名需要6个字符，请重新输入！')
#
#                 else:
#                     if username in user_list:
#                         print('你输入的用户名已注册，请重新输入')
#                     else:
#                         print(f"你输入的用户名可以正常注册：{username}")
#
#
# username = input("请输入你要查询的用户名；")
# user_check(username)
# 方法二
while True:
    username = input("请输入用户名：")
    with open("p077_users.txt") as f:
        users = [name.strip() for name in f.readlines()]

    if len(username) < 6:
        print("长度小于6位，请重新输入")
        continue

    if username in users:
        print("用户名已存在，请重新输入")
        continue
    else:
        print("用户名检测通过")
        break
