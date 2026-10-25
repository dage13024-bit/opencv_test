# 利用宽高比，面积和倾斜角度筛选框选矩形
import cv2
import numpy as np

# 制作底图，三个方块
img = np.zeros((400,600,3),np.uint8)
img[50:250,50:100] = (0,0,255) #50x200
img[100:200,150:250] = (0,0,255) #100x100
rect = ((350,150),(50,200),25) #50x200
points = np.intp(cv2.boxPoints(rect))
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
    rect = cv2.minAreaRect(contour)
    (cx,cy),(w,h),angle = rect
#     print(rect)
# ((199.5, 149.5), (99.0, 99.0), -90.0)
# ((74.5, 149.5), (199.0, 49.0), -90.0)
# ((349.5, 149.5), (201.4971160888672, 50.49650573730469), -65.22486114501953)
# 我根据输出调整了tile的判别方法，我做这个实验用的另外的电脑，环境不同
    if min(w,h) == 0:
        continue
    # 防止除零错误
    ratio = max(w,h)/min(w,h)
    # 不要用//向下取整
    if w < h:
        tile = angle
    else:
        tile = angle + 90
    tile = abs(tile)
    if ratio < 2.5:
        continue
    if tile > 35:
        continue
    points = np.intp(cv2.boxPoints(rect))
    cv2.drawContours(img,[points],0,(255,0,0),3)

cv2.imshow("Mask",mask)
cv2.imshow("Img",img)
cv2.waitKey(0)