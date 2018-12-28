# 迭代器
# list1 = [1,2,3,4,5]
# a = iter(list1)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(next(a))
# # print(next(a))
# print()
# 生成器 含有 yield 的函数 即含有 yield 的迭代器
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

for i in frange(10, 20, 0.5):
    print(i)