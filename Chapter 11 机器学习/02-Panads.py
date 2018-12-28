# Pandas 用于数据预处理和数据清洗
# 优点：1.自动对齐显示数据 2.灵活处理数据 3。使用SQL语句
from pandas import Series, DataFrame
import pandas as pd


obj = Series([2,3,5,-2])
# print(obj)
# print(obj.values)
# print(obj.index)

obj2 = Series([2,31,412,2], index=['a','b','c','q'])
# print(obj2)
# obj2['q'] = 8
# print(obj2)
# print('a' in obj2)

# 导入字典
# sdata = {'a':23, 'b':3443, 'c':2442}
# obj3 = Series(sdata)
# print(obj3)
# obj3.index = ['afs','fds','dsf'] #
# print(obj3)


# DataFrame 操作多维数组
data = {'city':['a', 'b', 'c'],
        'year':[2017, 2014, 2015],
        'pop':[1.6, 5.9, 8.1]}
frame = DataFrame(data)
print(frame)

frame2 = DataFrame(data, columns=['year', 'city', 'pop']) # 排序 列互换
print(frame2)

# 降维
print(frame2.year)
print(frame2['city'])

frame2['new'] = 100 # 生成新列
print(frame2)

frame2['cap'] = frame2.city == 'a'

print(frame2)

print('-------------------')
pop = {
    'beijing': {2018:1.5, 2010:3.6},
    'shanghai': {2018:3.10, 2010:5.3}
}
frame3 = DataFrame(pop)
print(frame3.T) # 转置
print(frame3)

print('------填充数据------')
obj4 = Series([3,4,4,5], index=['a', 'c', 'w', 'p'])
obj5 = obj4.reindex(['a','b','c','d','e'])
print(obj5)
obj6 = Series(['acc', 'qwex', 'cvx'], index=[0,2,4])
print(obj6.reindex(range(6), method='ffill'))
print(obj6.reindex(range(6), method='bfill'))


# 删除缺失值
from numpy import nan as NA

print('删除缺失值-----------')
data = Series([1, NA, 2])
print(data)
print(data.dropna())