"""
实现python代码，输出hello，停顿1秒；输出hello，停顿2秒；输出hello，停顿3秒；
打印4次hello，然后退出循环：
"""
# import time
#
# i = 1
# while True:
#     if i <= 4:
#         print('hello')
#         time.sleep(i)
#         i += 1
#     else:
#         break
# print('再见！')
# 方法二
import time

i = 0
while True:
    i = i + 1
    print("Hello")
    if i > 3:
        print("End of loop")
        break
    time.sleep(i)


