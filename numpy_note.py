import numpy as np

a1 = np.array([[2, 3], [3, 4]])
a2 = np.array([[0, 1], [2, 3]])
a3 = np.arange(4).reshape(2, 2)  # 重塑一个2乘2矩阵
# print(a1*a2)    # 各项相乘
# print(a1+a2)
# print(np.dot(a1, a2))  # 矩阵乘法
a4 = np.random.random((2, 4))
np.sum(a4)            # 所有元素求和
np.sum(a4, axis=1)    # 每行求和（几行返回几个值）
np.min(a4)            # 所有元素最小,每行求和（几行返回几个值）
np.min(a4, axis=0)    # 每列求最小（几列返回几个值）
np.max(a4)


b1 = np.arange(2, 11).reshape(3, 3)
# print(b1)
# print(np.argmax(b1))  # 最大值索引  同样可以选择行列数
# print(np.mean(b1))  # 平均值
# # print(np.diff(b1))  # 同行相邻元素差值
# print(np.sort(b1))  # 同行排列
# # # print(b1.T)  # 矩阵转置  ，或者np.transpose(b1)
b2 = np.arange(14, 2, -1).reshape(3, 4)  # 步长为负一
# print(np.clip(b2, 5, 9))  # 在五和九之间保留  小于五则变为五，大于9则变为9
#############################################################################
# 索引
# print(b2)
# print(b2[1][1])       # 索引第二行 第二列
# print(b2[:, 1])       # 索引第二列所有数
# print(b2[1, 1:3])     # 索引第二行，第二列，第三列
# for row in b2:
#     print(row)          # 打印所有行
# for column in b2.T:
#     print(column)       # 打印所有列
# print(b2.flatten())     # 讲b2变成一排迭代器
# for item in b2:         # 打印
#     print(item)

#######################################################################
# 合并
c1 = np.array([1, 1, 1])
c2 = np.array([2, 2, 2])
c3 = np.vstack((c1, c2))   # vertical stack  ,将c1 c2上下合并
c4 = np.hstack((c1, c2))     # horizontal stack ,  左右
# print(c4)
# print(c1[:, np.newaxis])  # 将c1变成纵向
c6 = np.array([1, 1, 1])[:, np.newaxis]  # 也可以直接这么用
c5 = np.concatenate((c1, c2, c1, c2), axis=0)  # 多矩阵合并，并可以改变合并方向
#################################################################
# 分割
d1 = np.arange(12).reshape(3, 4)
print(np.split(d1, 2, axis=1))  # 矩阵 分成几块，什么方向 1为横向
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#                     [ 6,  7],
#                      [10, 11]])]
# print(np.array_split(d1, 2, axis=1))  # 可以进行不等量分割
# print(np.vsplit(d1, 3))
# print(np.hsplit(d1, 2))
d2 = d1.copy()  # 将d1的值给d2但不关联






