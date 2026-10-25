
import math
# 计算返回归一化的点积，有零向量时返回none
def normalized_dot(u, v):
    # 1. 计算向量长度
    length_u = math.hypot(u[0],u[1])
    length_v = math.hypot(v[0],v[1])
    # 2. 检查零向量
    if length_u == 0 or length_v ==0:
        return None
    # 3. 计算点积
    dot = u[0]*v[0]+u[1]*v[1]
    # 4. 归一化点积
    cos_theta = dot / (length_u * length_v)   
    # 5. 返回归一化点积
    return cos_theta

print(normalized_dot((1, 0), (1, 0)))    # 1.0
print(normalized_dot((1, 0), (0, 1)))    # 0.0
print(normalized_dot((1, 0), (-1, 0)))   # -1.0
print(normalized_dot((0, 0), (1, 1)))    # None
