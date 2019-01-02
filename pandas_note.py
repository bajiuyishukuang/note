import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a1 = pd.Series([1, 2, 3])
dates = pd.date_range('20130101', periods=6)
print(a1, dates)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df1 = pd.DataFrame(np.arange(12).reshape(3, 4))

print(df.index)   #
print(df.columns)  #
print(df.values)  #
print(df.describe())  # 描述各种属性
print(df.T)   # 转置
print(df.sort_index(axis=1, ascending=False))  # 排序 对列及性能排序  以倒叙进行排序
print(df.sort_values(by='B'))  # 用B进行排序

print(df['A'], df.A)  # 按照A来排序，两种方式都行
print(df[0:3], df['20130102':'20130104'])  # 切片操作

# select by label: loc
print(df.loc['20130102'])  # 只选择制定标签
print(df.loc[:, ['A', 'B']])  # 打印多列
print(df.loc['20130102', ['A', 'B']])  # 某行，两列

# select by position: iloc
print(df.iloc[3])  # 第三行数据
print(df.iloc[3, 1])  #
print(df.iloc[3:5, 0:2])  # 切片操作
print(df.iloc[[1, 2, 4], [0, 2]])  # 指定操作

# mixed selection: ix
print(df.ix[0:3, ['A', 'C']])  # 混合筛选
# Boolean indexing
print(df[df.A > 0])  # 按条件筛选

df.iloc[2, 2] = 1111  # 修改元素
df.loc['2013-01-03', 'D'] = 2222
df.A[df.A > 0] = 0
df['F'] = np.nan  # f列全是nan
df['G'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130101', periods=6))


# 处理丢失数据
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how='any'))   # how={'any', 'all'}  只要有nan的列都删掉
print(df.dropna(axis=0, how='all'))  # 全部等于nan才删掉
print(df.fillna(value=0))  # 把nan数据填上0
print(pd.isnull(df))  # 缺失的为true


# read from
data = pd.read_csv('student.csv')
print(data)

# save to
data.to_pickle('student.pickle')

# concatenating
# # ignore index
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # 忽略前面的相同索引 直接进行重新排列

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res = pd.concat([df1, df2], axis=1, join='outer')
res = pd.concat([df1, df2], axis=1, join='inner')

# join_axes
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])  # 合并之后  按照一的 index合并

# append
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
res = df1.append(df2, ignore_index=True)
res = df1.append([df2, df3])  # 同时加两个

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'], 'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on='key', )
print(res)

# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                              'key2': ['K0', 'K0', 'K0', 'K0'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
# res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # default for how='inner'
# how = ['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=['key1', 'key2'], how='left')  # 只有两个都相同 才取
print(res)

# indicator
df1 = pd.DataFrame({'col1': [0, 1], 'col_left':['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# give the indicator a custom name
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
# 把如何合并的进行 描述


# merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],'B': ['B0', 'B1', 'B2']}, index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],'D': ['D0', 'D2', 'D3']}, index=['K0', 'K2', 'K3'])
print(left)
print(right)
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
# 讲age 用boy 和girls的形式输出
print(res)

# join function in pandas is similar with merge. If know merge, you will understand join

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()  # 累加
data.plot()

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
data = data.cumsum()
# plot methods:
# 'bar'条形图, 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)

plt.show()