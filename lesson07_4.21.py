# 把点积判断垂直的逻辑封装成一个可重复使用的函数

import math

def is_perpendicular(u, v, threshold=0.15):
    # 1. 计算两个向量的长度
    length_u = math.hypot(u[0],u[1])
    length_v = math.hypot(v[0],v[1])
    # 2. 检查是否存在零向量
    if length_v == 0 or length_u == 0:
        return False
    # 3. 计算点积
    dot = u[0]*v[0]+u[1]*v[1]
    # 4. 计算归一化点积
    cos_theta = dot/(length_u*length_v)
    # 5. 判断是否近似垂直
    if abs(cos_theta) < threshold:
        return True
    else:
        return False

print(is_perpendicular((1, 0), (0, 1)))      # True
print(is_perpendicular((1, 0), (1, 0)))      # False
print(is_perpendicular((20, -50), (100, 50))) # True
print(is_perpendicular((0, 0), (1, 1)))      # False

# 下面是ai优化后的代码
# import math

# def is_perpendicular(u, v, threshold=0.15):
#     length_u = math.hypot(u[0], u[1])
#     length_v = math.hypot(v[0], v[1])

#     if length_u == 0 or length_v == 0:
#         return False

#     dot = u[0] * v[0] + u[1] * v[1]
#     cos_theta = dot / (length_u * length_v)

#     return abs(cos_theta) < threshold