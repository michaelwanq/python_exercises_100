"""
编写Python代码，用户可以输入生日，程序打印活了多少天
"""
import datetime

birthday = input("请输入生日：")
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")

curr_datetime = datetime.datetime.now()
print(curr_datetime)

minus_datetime = curr_datetime - birthday_date

print(minus_datetime.days, "天")
