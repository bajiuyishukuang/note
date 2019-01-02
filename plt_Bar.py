import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# 向上的柱状图 然后是两种颜色的参数
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# 向下的柱状图 然后是两种颜色的参数
for x, y in zip(X, Y1):   # 用zip之后 每一步出来两个值
    # ha: horizontal alignment  横向对齐
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
# 前两个参数是标注的位置   内容  水平 竖直对齐的
for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()
