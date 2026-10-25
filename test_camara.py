import cv2

cap = cv2.VideoCapture(0)  # 0 表示电脑自带摄像头

while True:
    ret, frame = cap.read()   # 返回是否成功读取帧，frame是当前帧的图像数据
    if not ret:
        break
    cv2.imshow("frame", frame)  # 显示画面
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 q 退出
        break

cap.release() #释放摄像头
cv2.destroyAllWindows()  # 关闭所有OpenCV窗口