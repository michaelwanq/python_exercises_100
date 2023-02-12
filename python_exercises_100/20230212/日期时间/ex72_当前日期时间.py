"""
编写Python代码，输出当前的日期时间
形如：2022-05-14 18:49:18
"""
from datetime import datetime

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
