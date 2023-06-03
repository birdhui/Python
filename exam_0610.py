# 터틀 그래픽을 이용한 프로그램
# 1) onscreenclick()을 이용해 마우스 왼쪽 버튼 클릭시 반지름이 30픽셀인 circle을 색상이 다르게 구현
# 2) 클릭할 때 커서 위치가 1사분면에 있으면 red, 2사분면에 있으면 blue, 3사분면 green, 4사분면 purple색의 circle, 그 외에는 yellow로 구현
# 못풀었어요 ㅠㅠ
# 4사분면 위치는 알겠는데 그 위치 내에서
# 원이 안그려져서 못풀었습니다..

import turtle as t

def line(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def leftClick_red(x, y):
    t.penup()
    t.goto(x, y)
    if (t.xcor()>0 and t.xcor()<300) and (t.ycor()>0 and t.ycor()<300):
        t.pencolor('red')
    else:
        t.home()
    t.pendown()
    t.circle(30)

def leftClick_blue(x, y):
    t.penup()
    t.goto(x, y)
    if (t.xcor()<0 and t.xcor()>-300) and (t.ycor()>0 and t.ycor()<300):
        t.pencolor('blue')
    else:
        t.home()
    t.pendown()
    t.circle(30)

def leftClick_green(x, y):
    t.penup()
    t.goto(-x, -y)
    if (t.xcor()<0 and t.xcor()>-300) and (t.ycor()<0 and t.ycor()>-300):
        t.pencolor('green')
    else:
        t.home()
    t.pendown()
    t.circle(30)

def leftClick_purple(x, y):
    t.penup()
    t.goto(x, -y)
    if (t.xcor()>0 and t.xcor()<300) and (t.ycor()>0 and t.ycor()<300):
        t.pencolor('purple')
    else:
        t.home()
    t.pendown()
    t.circle(30)

def Click_yellow(x, y):
    t.penup()
    t.goto(x, y)
    if (t.xcor()>300) and (t.ycor()>300):
        t.pencolor('yellow')
    else:
        t.home()
    t.pendown()
    t.circle(30)

line(-300, 0, 300, 0)
line(0, -300, 0, 300)

t.onscreenclick(leftClick_red, 1)
t.onscreenclick(leftClick_blue, 1)
t.onscreenclick(leftClick_green, 1)
t.onscreenclick(leftClick_purple, 1)
t.onscreenclick(Click_yellow, 1)

t.done()