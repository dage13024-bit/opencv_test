# 目标：区分好上下点
def order_endpoints(p1, p2):
    if p1[1]<p2[1]:
        top =p1
        bottom =p2
    else:
        top =p2
        bottom =p1
    return top,bottom 

print(order_endpoints((225, 100), (175, 200)))
# ((225, 100), (175, 200))

print(order_endpoints((175, 200), (225, 100)))
# ((225, 100), (175, 200))
# 思考题：几乎水平不能根据y值判断上下端点，但是这样的灯条不会被我们放在
# 候选的灯条列表里面也不需要知道它的上下端点

# ai优化的代码
# def order_endpoints(p1, p2):
#     if p1[1] <= p2[1]:
#         return p1, p2
#     return p2, p1