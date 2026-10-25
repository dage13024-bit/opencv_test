import math

u = (20, -50)
v = (100, 50)
# 1. 计算点积
dot = u[0]*v[0]+u[1]*v[1]

# 2. 计算两个向量的长度
length_u = math.hypot(u[0],u[1])
length_v = math.hypot(v[0],v[1])

# 3. 计算归一化点积
cos_theta = dot/(length_u*length_v)

print("点积 =", dot)
print("归一化点积 =", cos_theta)

# 点积 = -500
# 归一化点积 = -0.08304547985373997
# 归一化就是计算它俩夹角的cos值，越垂直越接近90度越为0，所以我们希望值靠近零

# A：长 100 像素，中心 (100,100)
# B：长 95 像素，中心 (300,100)
# 两根灯条的中心距离是多少？
# 两根灯条的平均长度是多少？
# 中心距离与平均长度的比值是多少？
center_distance = 200
avg_length = (100 + 95) / 2
distance_ratio = center_distance / avg_length
print(center_distance,avg_length,distance_ratio)
# 200 97.5 2.051282051282051