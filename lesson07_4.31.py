import cv2
import math
def rect_to_light(rect):
    # 1. 获取中心点
    (cx,cy),_,_ = rect
    # 2. 获取四个顶点
    points = cv2.boxPoints(rect)
    # 3. 计算 0-1 和 1-2 两条边的长度
    dx1 = points[0][0]-points[1][0]
    dy1 = points[0][1]-points[1][1]
    dx2 = points[1][0]-points[2][0]
    dy2 = points[1][1]-points[2][1]
    length_01 = math.hypot(dx1,dy1)
    length_12 = math.hypot(dx2,dy2)
    # 4. 找到长边，并保存对应的方向向量
    if length_01 > length_12:
        length = length_01
        direction = (dx1,dy1)
    else:
        length = length_12
        direction = (dx2,dy2)
    # 5. 返回灯条字典
    return {"center": (cx, cy),"length": length,"direction": direction}

rects = [
    ((100, 150), (25, 100), 0),
    ((300, 150), (25, 95), 0),
    ((500, 150), (25, 30), 0)
]

lights = []
for rect in rects:
    # 调用 rect_to_light()
    light = rect_to_light(rect)
    # 将生成的字典加入 lights
    lights.append(light)

print(lights)
# 输出：[{'center': (100, 150), 'length': 100.0, 'direction': (np.float32(0.0), np.float32(100.0))}, 
# {'center': (300, 150), 'length': 95.0, 'direction': (np.float32(0.0), np.float32(95.0))},
#  {'center': (500, 150), 'length': 30.0, 'direction': (np.float32(0.0), np.float32(30.0))}]