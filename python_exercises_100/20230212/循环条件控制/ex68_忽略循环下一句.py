"""
如下代码只能输出一个Hello
while True:
    print("Hello")
    if 2 > 1:
        break
    print("Hi")
"""
while True:
    print("Hello")
    if 2 > 1:
        continue
    print("Hi")