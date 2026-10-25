# 目标：让判断是否垂直和判断是否平行的函数调用计算归一化点积的函数
import math
# 计算返回归一化的点积
def normalized_dot(u, v):
    length_u = math.hypot(u[0],u[1])
    length_v = math.hypot(v[0],v[1])
    if length_u == 0 or length_v ==0:
        return None
    dot = u[0]*v[0]+u[1]*v[1]
    cos_theta = dot / (length_u * length_v)   
    return cos_theta
# 判断两灯条长度是否相似
def is_length_similar(length1, length2, max_ratio=1.3):
    if length1 <= 0 or length2 <= 0:
        return False
    ratio = max(length1,length2)/min(length1,length2)
    return ratio <= max_ratio
# 获取灯条间距离和灯条长度比
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
# 判断灯条间距离和灯条长度比是否合理
def is_distance_reasonable(ratio, min_ratio=1.0, max_ratio=4.0):
    if (ratio <= 0) or (ratio is None):
        return False
    return ratio > min_ratio and ratio < max_ratio
# 判断是否近似垂直
def is_perpendicular(u, v, threshold=0.15):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False
    return abs(cos_theta) < threshold
# 判断是否近似平行
def is_parallel(u, v, threshold=0.98):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False  
    return abs(cos_theta) > threshold

light_A = {
    "center": (100, 100),
    "length": 100,
    "direction": (0, 100)
}

light_B = {
    "center": (300, 100),
    "length": 95,
    "direction": (0, 95)
}

light_C = {
    "center": (350, 100),
    "length": 30,
    "direction": (0, 30)
}
light_D = {
    "center": (100, 100),
    "length": 100,
    "direction": (-14, 100)
}

light_E = {
    "center": (300, 100),
    "length": 100,
    "direction": (14, 100)
}


def is_valid_pair(light1, light2):
    # 1. 检查两根灯条长度是否相似
    is_len_sim = is_length_similar(light1["length"],light2["length"])
    if not is_len_sim:
        return False
    # 2. 计算中心距离比例
    ratio = get_distance_ratio(light1["center"],light2["center"],light1["length"],light2["length"])
    # 3. 检查中心距离比例是否合理
    is_distance_valid = is_distance_reasonable(ratio)
    if not is_distance_valid:
        return False
    # 4.检查灯条是否近似平行
    is_par = is_parallel(light1["direction"],light2["direction"])
    if not is_par:
        return False
    # 5. 计算两根灯条的中心连线向量
    u = (light1["center"][0]-light2["center"][0],light1["center"][1]-light2["center"][1])
    # 6. 判断中心连线与两根灯条的长边是否都近似垂直
    is_per_1 = is_perpendicular(u,light1["direction"])
    is_per_2 = is_perpendicular(u,light2["direction"])
    # 7. 全部条件满足才返回 True
    return is_per_1 and is_per_2

print(is_valid_pair(light_A, light_B))  # True
print(is_valid_pair(light_A, light_C))  # False
print(is_valid_pair(light_D, light_E))  # False
