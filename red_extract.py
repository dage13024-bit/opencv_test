import cv2
import numpy as np  # 专门用来处理数组

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. 将 BGR 颜色空间转换成 HSV（色调饱和度明度），便于提取颜色
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. 定义红色的范围（注意：红色在HSV里跨了两个区间，0°和180°）
    # 区间1：浅红到正红（0~10）
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    # 区间2：紫红到深红（170~180）
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # 将两个区间合并成一个“红色面具”
    mask = cv2.bitwise_or(mask1, mask2)

    # 显示原画面和面具（白色=红色区域，黑色=其他）
    cv2.imshow("Original", frame)
    cv2.imshow("Red Mask", mask)

    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()