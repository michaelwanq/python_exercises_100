"""
如下代码会报错，你知道为什么吗，怎么修复？
def foo(a=1, b=2):
    return a + b

x = foo - 1
"""
# def foo(a, b):
#     return a + b
#
#
# x = foo(1,2) - 1
# print(x)
def foo(a = 1, b = 2):
    return a + b


x = foo() - 1
print(x)
