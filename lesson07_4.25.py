def is_length_similar(length1, length2, max_ratio=1.3):
    # 1. 检查两根灯条的长度是否有效
    if length1 <= 0 or length2 <= 0:
        return False
    # 2. 计算较长灯条与较短灯条的长度比例
    ratio = max(length1,length2)/min(length1,length2)
    # 3. 判断这个比例是否不超过 max_ratio
    return ratio <= max_ratio
    # 返回 True 或 False

print(is_length_similar(100, 95))       # True
print(is_length_similar(100, 30))       # False
print(is_length_similar(100, 100))      # True
print(is_length_similar(0, 100))        # False
print(is_length_similar(100, 80, 1.1))  # False
