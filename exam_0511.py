# 11. for문을 사용하여 5각형을 그리는 터틀 그래픽 프로그램

import turtle as t

t.pensize(5)
t.shape('turtle')       # 터틀 그래픽 모양

for i in range(0, 5):   # i가 0부터 4까지 반복
    t.fd(100)           # 오른쪽으로 144도
    t.rt(144)

t.done()