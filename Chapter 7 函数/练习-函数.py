'''
练习一 函数
创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
创建一个函数，传入n个整数，返回其中最大的数和最小的数
创建一个函数，传入一个参数n，返回n的阶乘
'''
# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
def func1():
    nums = input('请输入两个数字，以空格做分隔：')
    num1,*_,num2 = list(nums)
    print(int(num1) + int(num2))

# func1()


def func2(*a):
    print(max(list(a)))
    print(min(list(a)))

# func2(12,23,21,42,44,5,6546)


def func3(n):
    if n <=1 :
        return 1
    else:
        return n*func3(n-1)

a = func3(5)
print(a)

from functools import reduce
num4 = 3
b = reduce(lambda x, y: x * y, range(1,num4+1))
print(b)