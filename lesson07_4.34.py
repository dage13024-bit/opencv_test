# 目标：从灯条列表到配对好的装甲板列表
import cv2
import math
import numpy as np
# 先给出一大堆函数
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
def rect_to_tilt(rect):
    points = cv2.boxPoints(rect)
    dx1 = abs(points[0][0]-points[1][0])
    dy1 = abs(points[0][1]-points[1][1])
    dx2 = abs(points[1][0]-points[2][0])
    dy2 = abs(points[1][1]-points[2][1])
    length01 = math.hypot(dx1,dy1)
    length12 = math.hypot(dx2,dy2)
    if length01 > length12:
        tilt = math.degrees(math.atan2(dx1,dy1))
    else:
        tilt = math.degrees(math.atan2(dx2,dy2))
    return tilt
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
def is_parallel(u, v, threshold=0.98):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False  
    return abs(cos_theta) > threshold
def is_perpendicular(u, v, threshold=0.15):
    cos_theta = normalized_dot(u,v)
    if cos_theta is None:
        return False
    return abs(cos_theta) < threshold
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
# 制作底图
img = np.zeros((400,900,3),np.uint8)
img[50:350,50:100] = (0,0,255)
img[50:350,400:450] = (0,0,255)
img[200:350,700:750] = (0,0,255)
# hsv->mask
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower1 = (0,100,50)
upper1 = (10,255,255)
lower2 = (170,100,50)
upper2 = (179,255,255)
mask1 = cv2.inRange(hsv,lower1,upper1)
mask2 = cv2.inRange(hsv,lower2,upper2)
mask = cv2.bitwise_or(mask1,mask2)
# mask->contours
contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
lights = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 100:
        continue
    # contour->rect
    rect = cv2.minAreaRect(contour)
    (cx,cy),(w,h),angle = rect
    if min(w,h) == 0:
        continue
    ratio = max(w,h)/min(w,h)
    if ratio < 2.5:
        continue
    tilt = rect_to_tilt(rect)
    if tilt > 35: 
        continue
    # rect->light
    light = rect_to_light(rect)
    lights.append(light)
# lights->armor_pairs
armor_pairs = []
for i in range(len(lights)):
    for j in range(i+1, len(lights)):
        if is_valid_pair(lights[i],lights[j]):
            armor_pairs.append((lights[i],lights[j]))
            print(lights[i],lights[j])
print("候选灯条数量 =", len(lights))
print("候选装甲板数量 =", len(armor_pairs))


# 输出：
# {'center': (424.5, 199.5), 'length': 299.0, 'direction': (np.float32(0.0), np.float32(299.0))} 
# {'center': (74.5, 199.5), 'length': 299.0, 'direction': (np.float32(0.0), np.float32(299.0))}
# 候选灯条数量 = 3
# 候选装甲板数量 = 1

# 问题：同一根灯条 B 或 C 被多个装甲板候选共同使用，这一定是错误的吗？还是说我们需要进一步判断哪些配对更合理？
# 回答：有可能出现这样的情况，比如两块装甲板并排出现时。我们需要进一步判断哪些配对更合理
