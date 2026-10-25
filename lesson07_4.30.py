# 目标，通过rect返回我们想要的字典
import cv2
import math

rect = ((200, 150), (30, 120), 25)
points = cv2.boxPoints(rect)

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

light_A = rect_to_light(rect)
print(light_A)

# 输出：{'center': (200, 150), 'length': 119.99999163107515, 'direction': (np.float32(-50.714203), np.float32(108.75692))}
# 思考：通过dx，dy计算得来的tilt是没有保存方向信息的