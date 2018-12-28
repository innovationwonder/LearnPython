# 序列 string, list, tuple
# 成员关系 in / not in ， 连接 + ，重复 * ， 切片 [:]
# 目的：记录生肖，根据年份判断生肖
"""
思路：
1.面对的问题是？
2.在现实中 how to answer
3.how to program
"""

# 定义 12 生肖为一个字符串变量
chinese_zodiac = '猴、鸡、狗、猪、鼠、牛、虎、兔、龙、蛇、马、羊、'.replace('、','')
print(chinese_zodiac)
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])
# print(chinese_zodiac[0:-1])
# print(chinese_zodiac[:-1])

# 生肖 12 年一轮回，为了计算年份对应的生肖，对年份取 12 的余数
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])

print('猪' not in chinese_zodiac)
print(chinese_zodiac + chinese_zodiac + 'ffdsfd')
print(chinese_zodiac * 3)