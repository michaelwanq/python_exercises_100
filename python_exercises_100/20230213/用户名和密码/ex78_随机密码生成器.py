"""
编写Python代码，用户输入密码位数，给出一个随机密码生成
请输入密码位数：20
@X_>;HrLM9f?0Elg+q{o
"""
import string
import random

words = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

len = int(input("请输入密码位数："))
chosen = random.sample(words, len)
print(chosen,type(chosen))
password = "".join(chosen)
print(password)
