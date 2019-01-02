import matplotlib.pyplot as plt
import numpy as np


def f(a, b):
    # the height function
    return (1 - a / 2 + a ** 5 + b ** 3) * np.exp(-a ** 2 - b ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)  # 定义网格

# use plt.contour to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.get_cmap())
# 背景填充  x轴 y轴 z轴   等高线分成10部分（8+2）   透明度  然后将不同的颜色

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)
# adding label
plt.clabel(C, inline=True, fontsize=10)
# 标注数字在高度上
# 线不穿过图像

plt.xticks(())
plt.yticks(())
plt.show()
