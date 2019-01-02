import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n)  # 正太分布
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, s=75, c=T, alpha=0.5)
# 用颜色来设置 color
plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore x ticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore y ticks

plt.show()
