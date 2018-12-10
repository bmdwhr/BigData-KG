# 简述：要求输入某年某月某日
# 提问：求判断输入日期是当年中的第几天，第几周，星期几？

import datetime

"""
da = input('sdfsdf:')
da1=datetime.datetime.strptime(da,'%y-%m-%d').date()
d=datetime.datetime.isocalendar(da1)
z=d[1]
x=d[2]
day=datetime.datetime.now().date()-da1
print (day,z,x)
"""

def which_day(year, month, day):
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    whichday = 0
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        list[1] = 29
    for i in range(1, month):
        if month == 1:
            print (day)
        whichday = whichday + list[i - 1]
    whichday = whichday + day
    print (whichday)


if __name__ == "__main__":
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入天："))
    which_day(year, month, day)







