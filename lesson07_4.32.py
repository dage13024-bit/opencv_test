# 目标：打通制作lights列表和列表配对的全流程
import cv2
import math
def normalized_dot(u, v):
    length_u = math.hypot(u[0],u[1])
    length_v = math.hypot(v[0],v[1])
    if length_u == 0 or length_v ==0:
        return None
    dot = u[0]*v[0]+u[1]*v[1]
    cos_theta = dot / (length_u * length_v)   
    return cos_theta
def is_length_similar(length1, length2, max_ratio=1.3):
    if length1 <= 0 or length2 <= 0:
        return False
    ratio = max(length1,length2)/min(length1,length2)
    return ratio <= max_ratio
def get_distance_ratio(center1, center2, length1, length2):
    if length1 <= 0 or length2 <= 0:
        return None
    dx = center2[0] - center1[0]
    dy = center2[1] - center1[1]
    center_distance = math.hypot(dx, dy)
    if center_distance == 0:
        return None
    avg_length = (length1 + length2) / 2
    return center_distance / avg_length
def is_distance_reasonable(ratio, min_ratio=1.0, max_ratio=4.0):
    if ratio is None or ratio <= 0:
        return False
    return min_ratio < ratio < max_ratio
def is_perpendicular(u, v, threshold=0.15):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False
    return abs(cos_theta) < threshold
def is_parallel(u, v, threshold=0.98):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False  
    return abs(cos_theta) > threshold
def is_valid_pair(light1, light2):
    is_len_sim = is_length_similar(light1["length"],light2["length"])
    if not is_len_sim:
        return False
    ratio = get_distance_ratio(light1["center"],light2["center"],light1["length"],light2["length"])
    is_distance_valid = is_distance_reasonable(ratio)
    if not is_distance_valid:
        return False
    is_par = is_parallel(light1["direction"],light2["direction"])
    if not is_par:
        return False
    u = (light1["center"][0]-light2["center"][0],light1["center"][1]-light2["center"][1])
    is_per_1 = is_perpendicular(u,light1["direction"])
    is_per_2 = is_perpendicular(u,light2["direction"])
    return is_per_1 and is_per_2
def rect_to_light(rect):
    (cx,cy),_,_ = rect
    points = cv2.boxPoints(rect)
    dx1 = points[0][0]-points[1][0]
    dy1 = points[0][1]-points[1][1]
    dx2 = points[1][0]-points[2][0]
    dy2 = points[1][1]-points[2][1]
    length_01 = math.hypot(dx1,dy1)
    length_12 = math.hypot(dx2,dy2)
    if length_01 > length_12:
        length = length_01
        direction = (dx1,dy1)
    else:
        length = length_12
        direction = (dx2,dy2)
    return {"center": (cx, cy),"length": length,"direction": direction}


rects = [
    ((100, 150), (25, 100), 0),
    ((300, 150), (25, 95), 0),
    ((500, 150), (25, 30), 0)
]

# 制作lights列表
lights = []
for rect in rects:
    light = rect_to_light(rect)
    lights.append(light)
# 列表配对
for i in range(len(lights)):
    for j in range(i+1, len(lights)):
        print("灯条配对:", lights[i], lights[j])
        print(is_valid_pair(lights[i],lights[j]))

# 输出：
# 灯条配对: {'center': (100, 150), 'length': 100.0, 'direction': (np.float32(0.0), np.float32(100.0))} {'center': (300, 150), 'length': 95.0, 'direction': (np.float32(0.0), np.float32(95.0))}
# True
# 灯条配对: {'center': (100, 150), 'length': 100.0, 'direction': (np.float32(0.0), np.float32(100.0))} {'center': (500, 150), 'length': 30.0, 'direction': (np.float32(0.0), np.float32(30.0))}
# False
# 灯条配对: {'center': (300, 150), 'length': 95.0, 'direction': (np.float32(0.0), np.float32(95.0))} {'center': (500, 150),'length': 30.0, 'direction': (np.float32(0.0), np.float32(30.0))}
# False