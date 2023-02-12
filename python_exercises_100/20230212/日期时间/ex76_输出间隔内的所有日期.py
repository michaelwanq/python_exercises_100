"""
编写代码，输入开始日期，结束日期，返回中间的所有日期

例如，输入：begin_date = "2022-05-14"，end_date = "2022-05-18"
打印如下内容：
['2022-05-14', '2022-05-15', '2022-05-16', '2022-05-17', '2022-05-18']
"""
import datetime

def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        date_list.append(begin_date)
        begin_date_object = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        days1_timedelta = datetime.timedelta(days=1)
        begin_date = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list

begin_date = input('请输入开始日期：')
end_date = input("请输入结束日期：")
date_list = get_date_range(begin_date, end_date)
print(date_list)
