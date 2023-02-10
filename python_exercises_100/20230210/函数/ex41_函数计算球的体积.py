"""
编写函数，计算球的体积
要求函数的参数半径r，有一个默认值10
然后用r=2为参数，调用函数得到结果
"""
import math
def circle(r=10):
    volume = (4 * math.pi * r ** 3) / 3
    return volume

print(circle(r=2))
