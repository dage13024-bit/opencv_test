# 利用points判断长边，计算倾斜角，不用minarearect返回的可能有问题的angle
import cv2
import math
import numpy as np

# 制作底图，三个方块
img = np.zeros((400,600,3),np.uint8)
img[50:250,50:100] = (0,0,255) #50x200
img[100:200,150:250] = (0,0,255) #100x100
rect = ((350,150),(50,200),25) #50x200
points = np.intp(cv2.boxPoints(rect)) #得到整形轮廓点
cv2.drawContours(img,[points],-1,(0,0,255),-1)

# 转hsv做mask
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower1 = (0,100,50)
upper1 = (10,255,255)
lower2 = (170,100,50)
upper2 = (179,255,255)
mask1 = cv2.inRange(hsv,lower1,upper1)
mask2 = cv2.inRange(hsv,lower2,upper2)
mask = cv2.bitwise_or(mask1,mask2)

# 得到并筛选mask的轮廓
contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 100:
        continue
    rect = cv2.minAreaRect(contour) #获得轮廓的最小外接矩形
    (cx,cy),(w,h),angle = rect
    if min(w,h) == 0:
        continue
    # 防止除零错误
    ratio = max(w,h)/min(w,h) #判断高宽比
    # 不要用//向下取整
    if ratio < 2.5:
        continue

    # if w < h:
    #     tile = angle
    # else:
    #     tile = angle + 90
    # tile = abs(tile)
    # 抛弃使用minarearect返回的angle来判断倾斜角
    
    # 利用points计算长边，和倾角
    points = cv2.boxPoints(rect)
    dx1 = abs(points[0][0]-points[1][0])
    dy1 = abs(points[0][1]-points[1][1])
    dx2 = abs(points[1][0]-points[2][0])
    dy2 = abs(points[1][1]-points[2][1])
    length01 = math.hypot(dx1,dy1)
    length12 = math.hypot(dx2,dy2)
    if length01 > length12:
        print("0-1是长边")
        tilt = math.degrees(math.atan2(dx1,dy1))
        print(tilt)
    else:
        print("1-2是长边")
        tilt = math.degrees(math.atan2(dx2,dy2))
        print(tilt)
    if tilt > 35:  #但是这里算出来的tilt只有正数，似乎丧失了左偏右偏的信息
        continue
    # 先后用面积，宽高比，倾斜角卡过后再画边框线
    # print(len(points))
    print("points =", points)
    print("type   =", type(points))
    print("len    =", len(points) if points is not None else "None")
    print("shape  =", np.array(points).shape)
    points = np.intp(points)
    cv2.drawContours(img,[points],-1,(255,0,0),3) #小心，他要的是整形的数组我之前没有这么做就错了

cv2.imshow("Mask",mask)
cv2.imshow("Img",img)
cv2.waitKey(0)