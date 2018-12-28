'''
练习二 循环语句的使用
使用for语句输出1-100之间的所有偶数
使用while语句输出1-100之间能够被3整除的数字
'''
# for i in range(1,101):
    # a = lambda x: i%2==0,i
    # print(lambda x: i%2==0,i)
    # if i%2 == 0:
        # print(i,end=' ')

i = 1
while i in range(1,101):
    if i%3 == 0:
        print(i)
    i += 1