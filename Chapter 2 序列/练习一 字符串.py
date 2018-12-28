'''
练习一 字符串
定义一个字符串Hello Python 并使用print( )输出
定义第二个字符串Let‘s go并使用print( )输出
定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
'''
a = 'Hello Python'
print(a)
b = "Let‘s go"
print(b)
c = '"The Zen of Python" -- by Tim Peters '
print(c)

'''
练习二 字符串基本操作
定义两个字符串分别为 xyz 、abc
对两个字符串进行连接
取出xyz字符串的第二个和第三个元素
对abc输出10次
判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
'''
a, b = 'xyz', 'abc'
print(a,b)
c = a[1:3]
print(c)
print('abc'*10)
if a in 'xyz' or 'abc':
    print(a)


'''
练习三 列表的基本操作
定义一个含有5个数字的列表

为列表增加一个元素 100

使用remove()删除一个元素后观察列表的变化

使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
'''
list1 = [1,2,3,4,5]
print(list1)
list1.append(100)
print(list1)
list1.remove(2)
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[-1])

'''
练习四 元组的基本操作
定义一个任意元组，对元组使用append() 查看错误信息
访问元组中的倒数第二个元素
定义一个新的元组，和 1. 的元组连接成一个新的元组
计算元组元素个数
'''
tuple1 = (1,2,3,4,5)
# tuple1.append()
print(tuple1[-2])
tuple2 = (2,3,4,51)
tuple3 = tuple1 + tuple2
print(tuple3.__len__())
print(len(tuple3))