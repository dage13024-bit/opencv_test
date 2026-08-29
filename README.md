一、test_camara.py会弹出来一个名为“frame”的窗口，里面是笔记本摄像头拍到的实时画面。按键盘 q 键，窗口关闭。
二、red_extract.py会弹出两个窗口一个名为“frame”一个名为“mask”，frame里面是笔记本摄像头拍到的实时画面。
mask里面是处理后的画面，frame中红色的区域在mask中显示为白色，frame中其他区域显示为黑色。
三、detect_red.py在red_extract.py的基础上增加了轮廓查找和绘制，用绿色的框框选目标并显示坐标。
四、armor_detection.py在detect_red.py的基础上增加了灯条的配对逻辑，用黄色的框框选目标并显示armor。
五。多了一个tryread.py的文件作用是验证环境配置成功了