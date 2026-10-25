# 目标：把两个选好的灯条的脚点找到
import cv2
import numpy as np

img = np.zeros((300, 400, 3), np.uint8)
# 得到灯条端点
def get_axis_endpoints(center, direction):
    p1 = (
    center[0] - direction[0] / 2,
    center[1] - direction[1] / 2
    )

    p2 = (
        center[0] + direction[0] / 2,
        center[1] + direction[1] / 2
    )
    return p1,p2
# 将灯条排序上，下
def order_endpoints(p1, p2):
    if p1[1] <= p2[1]:
        return p1, p2
    return p2, p1

def order_leftright(light1, light2):
    if light1["center"][0]<light2["center"][0]:
        return light1, light2
    return light2, light1

# 得到一对灯条的四个角点
def get_armor_corners(light1, light2):
    # 1. 判断哪根灯条在左边，哪根在右边
    left,right = order_leftright(light1,light2)
    # 2. 计算左侧灯条的两个长轴端点
    l_p1,l_p2 = get_axis_endpoints(left["center"],left["direction"])
    # 3. 调用 order_endpoints() 获取 left_top、left_bottom
    left_top,left_bottom = order_endpoints(l_p1,l_p2)
    # 4. 计算右侧灯条的两个长轴端点
    r_p1,r_p2 = get_axis_endpoints(right["center"],right["direction"])
    # 5. 获取 right_top、right_bottom
    right_top,right_bottom = order_endpoints(r_p1,r_p2)
    # 6. 按固定顺序返回四个角点
    # 左上 → 右上 → 右下 → 左下
    return [left_top,right_top,right_bottom,left_bottom]

light1 = {
    "center": (100, 150),
    "length": 100,
    "direction": (0, 100)
}

light2 = {
    "center": (300, 150),
    "length": 100,
    "direction": (0, -100)
}

# armor = get_armor_corners(light1,light2)
armor = get_armor_corners(light2,light1)
print(armor)

# 输出：
# [(100.0, 100.0), (300.0, 100.0), (300.0, 200.0), (100.0, 200.0)]