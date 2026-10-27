# 告白爱心.py
# 用 turtle 画一颗满满的心，向喜欢的女生告白
# 运行方式：python 告白爱心.py

import turtle
import math
import time


def setup_screen():
    turtle.setup(900, 700, 200, 100)
    turtle.title("❤ 告白 ❤")
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.pensize(20)
    turtle.hideturtle()


def heart(x, y, size, color_):
    """以 (x, y) 为中心画一颗实心爱心，size 控制大小"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color_)
    turtle.begin_fill()
    for i in range(0, 361):
        t = math.radians(i)
        px = 16 * math.sin(t) ** 3
        py = (13 * math.cos(t) - 5 * math.cos(2 * t)
              - 2 * math.cos(3 * t) - math.cos(4 * t))
        turtle.goto(x + px * size, y - py * size)
    turtle.end_fill()


def star(x, y, size):
    """画一颗金色小星星"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("gold")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def write_text(x, y, msg, color_, size, font="Microsoft YaHei", style="bold"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color_)
    turtle.write(msg, align="center", font=(font, size, style))


def main():
    setup_screen()

    # 1. 主角：大爱心
    heart(0, -20, 15, "deeppink")

    # 2. 大爱心上叠一颗小红心，更有层次
    heart(0, 60, 7, "red")

    # 3. 四角的小爱心点缀
    for hx, hy, hs in [(-300, 140, 4), (300, 140, 4), (-300, -140, 4), (300, -140, 4)]:
        heart(hx, hy, hs, "hotpink")

    # 4. 星空点缀
    for sx, sy, ss in [(-410, 310, 20), (410, 310, 20), (0, 320, 22),
                       (-200, 330, 14), (200, 330, 14)]:
        star(sx, sy, ss)

    # 5. 表白的话
    write_text(0, 175, "我喜欢你很久了，", "white", 28)
    write_text(0, 135, "做我的女朋友，好吗？", "gold", 24)
    write_text(0, -305, "—— from 一直偷偷喜欢你的我", "salmon", 12, "SimHei", "normal")

    # 6. 心跳效果：背景缓慢闪烁三下
    for _ in range(3):
        turtle.bgcolor("black")
        time.sleep(0.4)
        turtle.bgcolor("#1c0505")
        time.sleep(0.4)

    turtle.done()


if __name__ == "__main__":
    main()