# 目标，计算斜率
import numpy as np

p1 = (100, 50)
p2 = (120, 150)

dx = abs(p1[0]-p2[0])
dy = abs(p1[1]-p2[1])
r = dx/dy
print(dx,dy,r)
# 输出：20 100 0.2
# 回答：dy是除数，不能为零，dy为零，长边就是水平的了