# 目标：通过dx，dy计算倾斜角
import math

# dx = 20
# dy = 100
# 倾斜角 = 11.309932474020213
# dx = 0
# dy = 100
# 倾斜角 = 0.0
# dx = 100
# dy = 100
# 倾斜角 = 45.0
dx = 100
dy = 0
# 倾斜角 = 90.0
tilt = math.degrees(math.atan2(abs(dx), abs(dy)))

print("倾斜角 =", tilt)
# 思考：我不知道，但是我知道tan在-90到90度的图像，dy趋于零的时候比值趋于无穷，角度趋于90度