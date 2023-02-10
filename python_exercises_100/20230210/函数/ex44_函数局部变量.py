"""
如下代码会输出什么内容？为什么呢？
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())
"""
c = 1


def foo():
    c = 2  # 函数内部定义的局部变量优先级更高
    return c


c = 3
print(foo())
