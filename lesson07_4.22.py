# 目的：通过灯条中心点列表产生配对
lights = [(100, 100), (200, 100), (350, 150)]

for i in range(len(lights)):
    for j in range(i+1, len(lights)):
        print("灯条配对:", lights[i], lights[j])

# 问题1:j从i+1开始就好了
# 问题2:3根灯条是2+1种，4根灯条就是3+2+1种一共6种
# 我的疑问：现在好像都是用yolo先框处小车和装甲板，现在传统是不是只能用来处理yolo给的装甲板里面的
# 灯条角点了？