# 目标：通过中点和长边向量计算两端点
def get_axis_endpoints(center, direction):
    # 计算长轴两个端点
    p1 = (
    center[0] - direction[0] / 2,
    center[1] - direction[1] / 2
    )

    p2 = (
        center[0] + direction[0] / 2,
        center[1] + direction[1] / 2
    )
    # 返回 p1, p2
    return p1,p2

center = (200, 150)
# direction = (-50, 100)
# 端点1 = (225.0, 100.0)
# 端点2 = (175.0, 200.0)
direction = (50, -100)
# 端点1 = (175.0, 200.0)
# 端点2 = (225.0, 100.0)

# 交换正负号，端点顺序改变，代表的长轴线段不改变
p1, p2 = get_axis_endpoints(center, direction)

print("端点1 =", p1)
print("端点2 =", p2)