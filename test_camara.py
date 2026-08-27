import cv2

cap = cv2.VideoCapture(0)  # 0 表示电脑自带摄像头

while True:
    ret, frame = cap.read()   # 读取一帧
    if not ret:
        break
    cv2.imshow("frame", frame)  # 显示画面
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 q 退出
        break

cap.release()
cv2.destroyAllWindows()