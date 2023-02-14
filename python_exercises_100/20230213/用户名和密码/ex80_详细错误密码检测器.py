"""
编写Python代码，需要用户一直输入密码，直到满足如下条件才退出循环：
至少包含一个数字；
至少包含一个大写字母；
密码至少6位数；
实现效果如下，如果不满足条件会一直循环，注意会给出多个不满足的信息：
"""
while True:
    msgs = []
    psw = input("请输入密码: ")
    if not any([i.isdigit() for i in psw]):
        msgs.append("需要至少一位数字")
    if not any([i.isupper() for i in psw]):
        msgs.append("需要至少一位大写字母")
    if len(psw) < 6:
        msgs.append("需要至少6位密码")
    if len(msgs) == 0:
        print("密码检测通过")
        break
    else:
        print("密码不通过，有如下原因: ")
        for note in msgs:
            print("*", note)
