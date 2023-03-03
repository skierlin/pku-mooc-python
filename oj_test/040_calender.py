n = int(input())


def days_of_week(year, mon, day):
    list1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #闰年2月份为29天
    list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #平年2月份为28天
    date = 0
    years = 0

    lst_days = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday"
    ]

    if (year % 4 == 0) & (year % 100 != 0) or year % 400 == 0:
        if mon in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                print('Illegal')
                return
        elif mon == 2:
            if day < 1 or day > 29:
                print('Illegal')
                return
        elif mon in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                print('Illegal')
                return
        else:
            print('Illegal')
            return
    else:
        if mon in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                print('Illegal')
                return
        elif mon == 2:
            if day < 1 or day > 28:
                print('Illegal')
                return
        elif mon in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                print('Illegal')
                return
        else:
            print('Illegal')
            return

    #输入的年份大于等于2018年的判断过程如下:
    if year >= 2018:
        for j in range(2018, year):
            if (j % 4 == 0) & (j % 100 != 0) or j % 400 == 0:  #闰年
                years += 366
            else:  #平年
                years += 365  #闰年天数加366天,平年加365天

        if ((year % 4) == 0) & ((year % 100) != 0) or ((year % 400) == 0):
            for i in range(mon - 1):
                date += list1[i]  #闰年月份按list1相加
            days = date + day
        else:
            for i in range(mon - 1):
                date += list2[i]  #平年月份按list2相加
            days = date + day

        total = days + years
        ji = total % 7  #参考日期是2018年1月1号是星期一

        #由于"ji=0"时,输出的结果是"星期0",因此对"ji"进行了判断,使"ji=0"时输出的结果为"星期7"
        print(lst_days[ji])

    #输入的年份小于2018年的判断过程如下:
    else:
        for j in range(year + 1, 2018):
            if (j % 4 == 0) & (j % 100 != 0) or j % 400 == 0:
                years += 366
            else:
                years += 365

        if ((year % 4) == 0) & ((year % 100) != 0) or ((year % 400) == 0):
            for i in range(mon - 1, 12):
                date += list1[i]
            days = date - day + 1
        else:
            for i in range(mon - 1, 12):
                date += list2[i]
            days = date - day + 1

        total = days + years
        ji = total % 7
        print(lst_days[(8 - ji)%7])


for i in range(n):
    year, mon, day = map(int, input().split())
    days_of_week(year, mon, day)
