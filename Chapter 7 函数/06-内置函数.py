# filter()， map(), reduce(), zip()


alist = [1,2,3,4,5]
blist = [1,2,3,4,5]

# filter()
a = list(filter(lambda x:x>3, alist)) # 筛选出 列表中符合条件的元素并转换成列表
# print(a)

# map()
b = list(map(lambda x,y:x+y, alist,blist)) # 将两个列表中的元素按照函数处理并转换成列表
# print(b)

# reduce()
from functools import reduce
c = reduce(lambda x,y:x+y, alist, 2) # 使用数字2 和 alist中的第一个元素相加，继续使用结果与alist的第二个元素相加，最后返回和
# print(c)

# zip()
d = zip(alist,blist) # 将两个列表合并
for i in d:
    print(i)


dicta = {'a':'aa', 'b':'bb'}
dictb = zip(dicta.values(), dicta.keys()) # 将字典的键和值互换
# print(dictb)
for i in dictb:
    # print(i)
    pass