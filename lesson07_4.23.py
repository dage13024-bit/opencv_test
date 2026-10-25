# 目标：封装函数，函数计算并返回两个灯条之间的距离和长度比例
import math

def get_distance_ratio(center1, center2, length1, length2):
    # 第一步：计算两个中心点的距离
    u = (abs(center1[0]-center2[0]),abs(center1[1]-center2[1])) #计算中心向量
    center_length = math.hypot(u[0],u[1]) #计算向量长度
    # 第二步：计算两根灯条的平均长度
    avg_length = (length1+length2)/2
    # 第三步：处理不合法的灯条长度
    if center_length == 0 or length1 <= 0 or length2 <= 0:
        print("灯条不符合配对要求或灯条长度不合法，返回值为-1")
        return -1
    # 第四步：返回距离比例
    return center_length/avg_length

print(get_distance_ratio((100, 100), (300, 100), 100, 95))
# 约 2.0513

print(get_distance_ratio((100, 100), (150, 100), 100, 100))
# 0.5

print(get_distance_ratio((100, 100), (300, 100), 0, 0))
# 应该安全处理，而不是发生 ZeroDivisionError
# 思考：仅仅根据这个比例无法知道它们具有相似的相对间距，我们不知道灯条是否平行，如果平行那我认为它们确实有相似的相对间距
# 距离很近肯定是不能认为它们能组成装甲板，也许是拖影，不同角度的装甲板确实会导致两灯条的距离和长度比不同，如果很近，那么应该认为装甲板转过去了，应该看下一块板子