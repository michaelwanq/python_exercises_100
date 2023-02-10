"""
如下代码会报错，你知道为什么吗，怎么修复错误？
def foo(a, b):
    print(a + b)

x = foo(2, 3) * 10
"""
def foo(a, b):
    result = a + b
    return result

print(foo(2, 3) * 10 )