import matplotlib.pyplot as plt
import numpy as np


# 描点
x1 = [0, 2, 2, 0]
y1 = [0, 0, 2, 2]
x2 = [4, 6, 6, 4]
y2 = [4, 4, 6, 6]
x = np.arange(0, len(x1))+1
my_x_ticks = np.arange(1, 14, 1)
plt.xticks(my_x_ticks)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 创建画图窗口
fig = plt.figure()
# 将画图窗口分成1行1列，选择第一块区域作子图
ax1 = fig.add_subplot(1, 1, 1)
# 画散点图
ax1.scatter(x1, y1, label="w1", s=5, c='k', marker='o')
ax1.scatter(x2, y2, label="w2", s=5, c='r', marker='x')
# marker设置标记形状 markersize设置标记大小
# plt.plot(x, x1, label='list1', marker="o", markersize=10)
# plt.plot(x, y1, label='list2', marker="x", markersize=8)

y = -x+6
# 画出坐标轴
ax1.plot(x, y, label="判别界面")
# 添加图例
plt.legend(loc="upper left")
plt.show()
