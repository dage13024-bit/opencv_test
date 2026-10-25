# 目标：识别长边
import cv2
import numpy as np
import math

# 构建矩形，获取角点
rect = ((200, 150), (30, 120), 25)
points = cv2.boxPoints(rect)
# 利用脚点判断一条长边
dx1 = abs(points[0][0]-points[1][0])
dy1 = abs(points[0][1]-points[1][1]) # 第一个和第二个脚点的dx，dy
dx2 = abs(points[1][0]-points[2][0])
dy2 = abs(points[1][1]-points[2][1]) # 第二个和第三个脚点的dx，dy
lenth01 = math.hypot(dx1,dy1) 
lenth12 = math.hypot(dx2,dy2) # hypot计算二维向量的长度
if lenth01 > lenth12:
    print("0-1是长边")
else:
    print("1-2是长边")

# 输出：0-1是长边
# 思考题：当然可以，知道0-1是长边直接利用tilt = math.degrees(math.atan2(dx1,dy1))就可以得到倾斜角了
# 我们的dx，dy都是正值，所以不用担心算出来负的角度