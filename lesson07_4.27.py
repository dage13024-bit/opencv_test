# 目标：封装一个检查平行的函数
import math

def is_parallel(u, v, threshold=0.98):
    # 1. 计算两个向量的长度
    length_u = math.hypot(u[0],u[1])
    length_v = math.hypot(v[0],v[1])
    # 2. 检查零向量
    if length_u == 0 or length_v ==0:
        return False
    # 3. 计算点积
    dot = u[0]*v[0]+u[1]*v[1]
    # 4. 归一化点积
    cos_theta = dot / (length_u * length_v)   
    # 5. 判断是否近似平行
    return abs(cos_theta) > threshold

print(is_parallel((0, 100), (0, 95)))       # True
print(is_parallel((0, 100), (0, -95)))      # True
print(is_parallel((1, 0), (0, 1)))          # False
print(is_parallel((-14, 100), (14, 100)))   # False
print(is_parallel((0, 0), (0, 100)))        # False