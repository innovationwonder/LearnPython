'''
机器学习通用处理步骤：
    1.数据的采集:通过调查问卷或者网络信息搜集整理
    2.数据的预处理：统一格式
    3.数据的清洗：删减部分数据
    4.数据的建模：使用算法喂给机器
    5.数据的测试：对结果进行测试，通过测试则建模
Numpy库 用于数据预处理，高性能科学计算和数据分析
'''
import numpy as np


arr1 = np.array([2, 3, 4])
# print(arr1)
# print(arr1.dtype)

arr2 = np.array([1.23, 23.2, 2.5])
# print(arr2)
# print(arr2.dtype)
# print(arr2 + arr1)
# print(arr2*5)
print('Numpy 数组与标量进行算术运算')
# data = [[1,2,3], [4,5,6]]
# arr3 = np.array(data)
# # print(arr3)
#
# # a = np.zeros(10)
# # print(a)
# b = np.zeros((3, 5)) # 3 行 5 列 0矩阵
# print(b)
#
# d = np.ones((2,3)) # 全为 1 的矩阵
# print(d)
#
# f = np.empty((2,3,4)) #
# print(f)

arr4 = np.arange(10)
print(arr4)
# arr4[5:8] = 10

arr_slice = arr4[5:8].copy()
# print(arr_slice)
arr_slice[:] = 15

print(arr_slice)
print(arr4)
