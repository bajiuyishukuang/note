import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
#
# plt.figure()  # 写出背景属性 下面有几个plt 有几条曲线
# plt.plot(x, y1)


plt.figure(num=3, figsize=(8, 5),)  # 序号是 3 长是8 宽是5
l1, = plt.plot(x, y2, label='up')
# plot the second curve in this figure with certain parameters
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
# 线宽1.0  虚线  线的名字叫down


# 设置坐标轴属性
# set x limits
plt.xlim((-1, 2))  # x坐标轴范围
plt.ylim((-2, 3))
plt.xlabel('I am x')  # x轴描述（参数）
plt.ylabel('I am y')

# set new sticks
new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
plt.xticks(new_ticks)  # x轴每个标的数目
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# -2对应 是really 一一对应加上 r是正则表达  两边加$是换字体
# to use '$ $' for math leetcode and nice looking, e.g. '$\pi$'


# 更改坐标轴位置
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#  spines（脊梁）表示图片四个边框  右边和上边的图片消失
ax.xaxis.set_ticks_position('bottom')
# ACCEPTS: [ 'top' | 'bottom' | 'both' | 'default' | 'none' ]
# 新坐标系的x = 原坐标系的bottom
ax.spines['bottom'].set_position(('data', 0))
# the 1st is in 'outward' | 'axes' | 'data'
# axes: percentage of y axis
# data: depend on y data
# 将y轴的哪个点 作为和x轴的交点 Date后面是0就是y轴的0点
ax.yaxis.set_ticks_position('left')
# ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]
ax.spines['left'].set_position(('data', 0))
# 将y轴放在x轴的零点的位置


# 图例
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')
# 图例有l1 and l2, l1的图例是aaa，l2的是bbb，地点选择默认最好的地方，如果只有l1  那就只有这一个标注

# 注解
x0 = 1
y0 = 2*x0+1
plt.scatter(x0, y0, s=50, c='b')
# scatter 散点图  简写 size是50  color是blue
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)
# 两点确定一条线段(先输入两个横坐标，然后输入两个纵坐标 颜色是black 虚线 线宽是 2.5
# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#  打出2x+1=y0这句话   描述的点是x0 y0  基于坐标原点（date）
# 文字内容基于选点 30 -30的位置 箭头选择 ->
# 箭头弧度是 arc3


# method 2:
########################
plt.text(-3.7, 3, r'$This\ is\ the\ some\ leetcode. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
# 开始于-3.7,3这个点 大小  颜色

# 能见度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # set zorder for ordering the plot in plt 2.0.2 or higher
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.8, zorder=2))


plt.show()

#########

