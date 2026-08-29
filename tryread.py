import cv2
import os

image = cv2.imread("./img/demo.png")        #建议使用绝对路径imread()函数用于读取图片，第一个参数是图片路径，第二个参数是读取模式，默认是彩色模式
if image is None:                           #找不到并不会输出错误，而是返回None
    print("错误：无法读取图片，请检查路径")
    print("当前路径为：", os.getcwd())        #打印程序寻找文件的目录
    exit(1)
else:
    cv2.imshow("demo", image)               #imshow()函数用于显示图片，第一个参数是窗口名称，第二个参数是图片数据
    cv2.waitKey(0)                          #waitKey()函数用于等待键盘输入，参数是等待时间，单位是毫秒，0表示无限等待
    cv2.destroyAllWindows()                 #destroyAllWindows()函数用于销毁所有窗口