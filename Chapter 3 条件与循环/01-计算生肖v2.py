# 记录生肖，根据年份判断生肖
chinese_zodiac = '猴、鸡、狗、猪、鼠、牛、虎、兔、龙、蛇、马、羊、'.replace('、','')
# print(chinese_zodiac)
# year = int(input('请用户输入年份：'))
# if (chinese_zodiac[year % 12]) == '狗':
#     print('狗年运势···')

# for cz in chinese_zodiac:
#     print(cz)

# 遍历1-12
# for i in range(1,13):
#     print(i, end=' ')

# 遍历0-12
# for i in range(13):
#     print(i, end=' ')

# for year in range(1990,2019):
#     print('%s 年的生肖是 %s' %(year,chinese_zodiac[year % 12]))

import time
num = 9
while True:
    # print('a')
    num = num + 1

    # if num > 10:
    if num == 10:
        continue

    print(num)
    # time.sleep(1)

