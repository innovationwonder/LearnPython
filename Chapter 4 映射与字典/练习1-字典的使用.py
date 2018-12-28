'''
练习一 字典的使用
定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
取出字典中关键字为d的值
'''
adict = {}
adict['a'] = 1
adict['b'] = 2
adict['c'] = 3
adict['d'] = 4

adict['c'] = 'ckae'
print(adict)

print(adict['d'])

'''
练习二 集合的使用
将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
将字符串hello转换为集合
'''
astr = 'hello'
print(set(astr))
a = set(i for i in astr)
print(a)