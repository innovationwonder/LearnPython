zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 提示用户输入 月份和日期
month = int(input("请输入月份："))
day = int(input("请输入日期："))

# if判断
# for zd in range(len(zodiac_days)):
#     if zodiac_days[zd] >= (month,day):
#         print(zodiac_name[zd])
#         break
#
#     elif month == 12 and day > 23:
#         print(zodiac_name[0])
#         break

# while循环
n = 0
while zodiac_days[n] < (month,day):
    if month == 12 and day > 23:
            # print(zodiac_name[0])
            break
    n += 1
print(zodiac_name[n])