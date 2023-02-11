"""
实现python代码，输出hello，停顿1秒；输出hello，停顿2秒；输出hello，停顿3秒；
按此一直持续：
"""
import time

i = 0
while True:
    i += 1
    print('hello')
    time.sleep(i)
