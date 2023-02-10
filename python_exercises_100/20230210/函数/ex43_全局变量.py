"""
如下代码会输出什么内容？为什么呢？
c = 1
def foo():
    return c
c = 3
print(foo())
"""
c = 1


def foo():
    return c
# print(foo())  # 此时制定了函数，并没有调用

c = 3
print('*' * 10)
print(foo())
