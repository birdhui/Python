import turtle as t

def leftClick(x, y):
    t.pencolor('blue')
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(5):
        t.fd(50)
        t.rt(144)

t.onscreenclick(leftClick, 1)

t.done()