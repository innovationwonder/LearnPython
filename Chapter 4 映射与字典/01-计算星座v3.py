chinese_zodiac = '猴、鸡、狗、猪、鼠、牛、虎、兔、龙、蛇、马、羊、'.replace('、','')
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座') # u 表示Unicode
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 声明 2 个字典 用于记录生肖和星座的情况
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0
print(z_num)

z_num = {i:0 for i in zodiac_name}
print(z_num)

while True:
    # 提示用户输入 年月日
    year,month,day = int(input('请输入年份：')), int(input('请输入月份：')), int(input('请输入日期：'))

    # 输出生肖和星座
    n = 0
    while zodiac_days[n] < (month,day):
        if month == 12 and day > 23:
            break
        n += 1
    print('%s 月 %s 号的星座是%s'%(month, day,zodiac_name[n]))
    print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    # 输出统计信息
    for k in cz_num.keys():
        print('生肖 %s 有 %s 个' %(k,cz_num[k]))

    for j in z_num.keys():
        print('星座 %s 有 %s 个' %(j,z_num[j]))
