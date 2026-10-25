import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. 转HSV并提取红色掩码（就是你刚才成功的那一段）
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # ---- 🆕 新代码：轮廓查找与绘制（PDF 3.5节核心） ----
    # 2. 查找所有白色区域的轮廓（外轮廓）
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# contours, _：两个返回值。contours 是一个列表，每个元素是一个轮廓（由点组成的 NumPy 数组）；
# _ 是第二个返回值（层次结构），用下划线表示忽略。
# cv2.findContours()：从二值图像中查找轮廓。
# 第一个参数 mask：输入的二值图像（白色为前景）。
# 第二个参数 cv2.RETR_EXTERNAL：轮廓检索模式，只检测最外层轮廓，忽略内部嵌套。
# 第三个参数 cv2.CHAIN_APPROX_SIMPLE：轮廓近似方法，压缩水平、垂直和对角线段，仅保留端点，节省内存。

    # 3. 遍历每一个找到的轮廓
    for cnt in contours:
        # 计算轮廓面积，过滤掉太小的噪点（比如只有几个像素的白点）
        area = cv2.contourArea(cnt)
        if area > 100:  # 这个数值可以调，太小则忽略
            # 4. 获取包围该轮廓的矩形框（x, y, 宽, 高）
            x, y, w, h = cv2.boundingRect(cnt)

            # 5. 计算矩形的中心坐标
            cx = x + w // 2
            cy = y + h // 2

            # 6. 在原始画面上画一个绿色的矩形框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # 在中心画一个红色的小圆点
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            # 在矩形上方显示坐标文本
            cv2.putText(frame, f"({cx}, {cy})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 显示结果：左边原图带框，右边是黑白面具
    cv2.imshow("Detection Result", frame)
    cv2.imshow("Red Mask", mask)

    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()