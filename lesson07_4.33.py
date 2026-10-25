# 目标：从图像到自动生成灯条列表
import cv2
import math
import numpy as np

def rect_to_light(rect):
    (cx,cy),_,_ = rect
    points = cv2.boxPoints(rect)
    dx1 = points[0][0]-points[1][0]
    dy1 = points[0][1]-points[1][1]
    dx2 = points[1][0]-points[2][0]
    dy2 = points[1][1]-points[2][1]
    length_01 = math.hypot(dx1,dy1)
    length_12 = math.hypot(dx2,dy2)
    if length_01 > length_12:
        length = length_01
        direction = (dx1,dy1)
    else:
        length = length_12
        direction = (dx2,dy2)
    return {"center": (cx, cy),"length": length,"direction": direction}
def rect_to_tilt(rect):
    points = cv2.boxPoints(rect)
    dx1 = abs(points[0][0]-points[1][0])
    dy1 = abs(points[0][1]-points[1][1])
    dx2 = abs(points[1][0]-points[2][0])
    dy2 = abs(points[1][1]-points[2][1])
    length01 = math.hypot(dx1,dy1)
    length12 = math.hypot(dx2,dy2)
    if length01 > length12:
        tilt = math.degrees(math.atan2(dx1,dy1))
    else:
        tilt = math.degrees(math.atan2(dx2,dy2))
    return tilt
# 制作底图，三个方块
img = np.zeros((400,900,3),np.uint8)
img[50:350,50:100] = (0,0,255) #50x300
img[50:350,400:450] = (0,0,255) #50x300
img[200:350,700:750] = (0,0,255) #50x150

# 转hsv做mask
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower1 = (0,100,50)
upper1 = (10,255,255)
lower2 = (170,100,50)
upper2 = (179,255,255)
mask1 = cv2.inRange(hsv,lower1,upper1)
mask2 = cv2.inRange(hsv,lower2,upper2)
mask = cv2.bitwise_or(mask1,mask2)

# 得到mask的白色轮廓
contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# 将面积和高宽比合适的灯条添加到候选灯条列表
lights = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 100:
        continue
    rect = cv2.minAreaRect(contour)
    (cx,cy),(w,h),angle = rect
    if min(w,h) == 0:
        continue
    ratio = max(w,h)/min(w,h)
    if ratio < 2.5:
        continue
    #还利用倾斜角再筛选一轮
    tilt = rect_to_tilt(rect)
    if tilt > 35:  #但是这里算出来的tilt只有正数，似乎丧失了左偏右偏的信息
        continue
    light = rect_to_light(rect)
    lights.append(light)

print("候选灯条数量 =", len(lights))
print(lights)

# 输出：
# 候选灯条数量 = 3
# [{'center': (724.5, 274.5), 'length': 149.0, 'direction': (np.float32(0.0), np.float32(149.0))},
#  {'center': (424.5, 199.5), 'length': 299.0, 'direction': (np.float32(0.0), np.float32(299.0))},
#  {'center': (74.5, 199.5), 'length': 299.0, 'direction': (np.float32(0.0), np.float32(299.0))}]

# 思考题：我们在将单个灯条添加到候选灯条列表时要先经过一轮筛选，
# 主要是筛选掉面积过小，不易观察的噪声和长宽比例不符合灯条特征的样本，这能减少很多后续的计算量
# 当然我们可以在这里就通过dx，dy计算的tilt先筛一轮再加入候选灯条列表