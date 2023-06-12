import turtle as t

def line(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

# 반지름이 30인 circle 그리기 함수
def draw_circle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.circle(30)

# 마우스 클릭 이벤트 처리 함수
def on_click(x, y):
    if x >= 0 and y >= 0:
        draw_circle(x, y, "red")
    elif x < 0 and y >= 0:
        draw_circle(x, y, "blue")
    elif x < 0 and y < 0:
        draw_circle(x, y, "green")
    elif x > 0 and y < 0:
        draw_circle(x, y, "purple")
    else:
        if y > 0:  # 1사분면에 해당하는 경우
            t.pencolor("yellow")
            t.goto(x, y)
            t.penup()
        elif y < 0:  # 2사분면에 해당하는 경우
            t.pencolor("yellow")
            t.goto(x, y)
            t.pendown()

line(-300, 0, 300, 0)
line(0, -300, 0, 300)

t.onscreenclick(on_click)

t.mainloop()
