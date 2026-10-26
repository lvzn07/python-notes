import turtle

# 画布设置
turtle.setup(width=600, height=600)
turtle.title("红色爱心")

pen = turtle.Turtle()
pen.speed(2)       # 绘制速度慢，数值越小速度越慢
pen.pensize(12)    # 加粗线条
pen.color('red')
pen.hideturtle()

# 移动到爱心底部中点，保证整体居中
pen.penup()
pen.goto(0, -60)
pen.pendown()

# 只绘制一遍空心爱心
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)  # 左侧圆弧
pen.left(120)
pen.circle(-90, 200)  # 右侧圆弧
pen.forward(180)

turtle.done()
