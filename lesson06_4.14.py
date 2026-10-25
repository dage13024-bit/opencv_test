# 目标：观察点集的数据结构
import cv2
import numpy as np

rect = ((200, 150), (30, 120), 25)

points = cv2.boxPoints(rect)

print(points)
print("shape =", points.shape)
# 输出：
# [[161.04828  198.03918 ]
#  [211.76248   89.282265]
#  [238.95172  101.96081 ]
#  [188.23752  210.71774 ]]
# shape = (4, 2)

# points.shape 是多少？为什么是这个形状？
# 是一个4行两列的矩阵，四个点，一行一个x,y
# points[0] 表示什么？它包含几个数？
# 表示第一个点的x，y坐标
# 如果想计算 points[0] 和 points[1] 之间的水平坐标差 dx，你会怎么写？
# 可以points[0][0]-points[1][0]