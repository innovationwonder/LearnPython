'''
练习一 条件语句的使用
使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
'''
str1 = '1234567890'
if len(str1) == 10:
    print('等于10')
else:
    print('不等于10')

num = int(input('请输入一个1-40之间的数字：'))
if num in range(1,11):
    print('1-10')
elif num in range(11,21):
    print('11-20')
elif num in range(21,31):
    print('21-30')
elif num in range(31,41):
    print('31-40')