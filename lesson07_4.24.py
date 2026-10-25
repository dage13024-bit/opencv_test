# 目标：判断之前算的灯条对的长度和距离比值是否合理
def is_distance_reasonable(ratio, min_ratio=1.0, max_ratio=4.0):
    # 判断 ratio 是否有效
    if ratio <= 0:
        return False
    # 判断 ratio 是否处于合理范围
    if ratio > min_ratio and ratio < max_ratio:
        return True
    else:
        return False
    # 返回 True 或 False

print(is_distance_reasonable(2.05))  # True
print(is_distance_reasonable(0.1))   # False
print(is_distance_reasonable(6.0))   # False
print(is_distance_reasonable(-1))    # False
print(is_distance_reasonable(3.0, 2.0, 2.5)) # False
print(is_distance_reasonable(None))  # TypeError

# ai修改
# def is_distance_reasonable(ratio, min_ratio=1.0, max_ratio=4.0):
#     if ratio is None or ratio <= 0: #判断none应该放在前面，不然会短路，发生类型错误
#         return False
#     return min_ratio < ratio < max_ratio

# 我也不太明白为什么设置最小最大比例，是因为要符合透视规律吗？
# 距离比例过小时，两根灯条过于靠近，可能是同一个亮斑被分割成两个轮廓，也可能是相邻的其他发光结构。
# 距离比例过大时，两根灯条可能来自两块不同的装甲板，甚至不同的机器人。
# 距离比例处于合理区间时，才更有可能属于同一块装甲板。
