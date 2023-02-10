"""
如下代码的最后一行，会报错说NameError: name 'c' is not defined
怎样修复代码，让代码不报错，并且输出数值1？
def foo():
    c = 1
    return c
foo()
print(c)
"""


def foo():
    global c
    c = 1
    return c


foo()
print(c)
