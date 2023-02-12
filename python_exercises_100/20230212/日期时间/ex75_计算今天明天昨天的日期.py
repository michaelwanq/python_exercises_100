"""
编写代码，输出今天、昨天、明天、一周前的日期
可以编写个函数实现

如果今天是2022-05-14，输出形如：
2022-05-14 2022-05-13 2022-05-15 2022-05-07
"""
import datetime

def diff_days(days):
    print("*" * 10)
    pdate_obj = datetime.datetime.now()
    print('pdate_obj: ',pdate_obj)
    time_gap = datetime.timedelta(days=days)
    print('time_gap: ',time_gap)
    pdate_result = pdate_obj - time_gap
    print('pdate_result: ',pdate_result)
    return pdate_result.strftime("%Y-%m-%d")

print(diff_days(0), diff_days(1), diff_days(-1), diff_days(7))