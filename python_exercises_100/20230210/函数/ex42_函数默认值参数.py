"""
如下代码会报错，你知道为什么吗，怎么修复？
def foo(a=2, b):
    return a + b
"""


def foo(b, a=2):
    return a + b


print(foo(1))
