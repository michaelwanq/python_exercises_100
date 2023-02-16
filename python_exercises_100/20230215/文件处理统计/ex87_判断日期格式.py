"""
编写函数date_is_right，判断日期是不是 YYYY-MM-DD 的格式
如果是返回True，否则返回False
测试结果形如：
2021-05-20 True
202-05-20 False
2021/05-20 False
20210520 False
20a10520 False
"""

import re


def date_is_right(date):
    return re.match(r"\d{4}-\d{2}-\d{2}", date) is not None


print("2021-05-20", date_is_right("2021-05-20"))
print("202-05-20", date_is_right("202-05-20"))
print("2021/05-20", date_is_right("2021/05-20"))
print("20210520", date_is_right("20210520"))
print("20a10520", date_is_right("20a10520"))
