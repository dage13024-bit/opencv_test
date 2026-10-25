import cv2
import os

image = cv2.imread("./img/demo.png")      
# cv2.imread()：OpenCV 中用于读取图像文件的函数。
# 第一个参数 "./img/demo.png"：图片路径，./ 表示当前工作目录（即运行程序时的目录），img 是子文件夹，demo.png 是文件名。注释建议使用绝对路径以避免路径问题。
# 第二个参数省略，默认值为 cv2.IMREAD_COLOR，即以彩色模式（BGR 三通道）读取图片。
if image is None:                           #找不到并不会输出错误，而是返回None
    print("错误：无法读取图片，请检查路径")
    print("当前路径为：", os.getcwd())        #打印程序寻找文件的目录
    exit(1)  # 程序退出，返回错误码1    
else:
    cv2.imshow("demo", image)               #imshow()函数用于显示图片，第一个参数是窗口名称，第二个参数是图片数据
    cv2.waitKey(0)                          #waitKey()函数用于等待键盘输入，参数是等待时间，单位是毫秒，0表示无限等待
    cv2.destroyAllWindows()                 #destroyAllWindows()函数用于销毁所有窗口