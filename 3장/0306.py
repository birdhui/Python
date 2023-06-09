import turtle as t

t.pensize(10)

t.pencolor('blue')
t.penup()
t.goto(-120, 0)
t.pendown()
t.circle(50)

t.pencolor('black')
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(50)

t.pencolor('red')
t.penup()
t.goto(120, 0)
t.pendown()
t.circle(50)

t.pencolor('orange')
t.penup()
t.goto(-60, -50)
t.pendown()
t.circle(50)

t.pencolor('green')
t.penup()
t.goto(60, -50)
t.pendown()
t.circle(50)

t.done()