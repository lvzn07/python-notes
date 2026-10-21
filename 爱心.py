# 红色控制码
RED = '\033[31m'
RESET = '\033[0m'

# 爱心数学方程：(x²+y²-1)³ - x²y³ = 0
for y in range(15, -15, -1):
    line = ""
    for x in range(-28, 28):
        # 校准缩放比例，让爱心形状更正
        x_scale = x * 0.05
        y_scale = y * 0.1
        if (x_scale**2 + y_scale**2 - 1)**3 - x_scale**2 * y_scale**3 <= 0:
            line += RED + '❤' + RESET
        else:
            line += " "
    print(line)

