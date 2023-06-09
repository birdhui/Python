# 13. 2개의 중첩 for문을 사용하여 각 변의 길이가 100픽셀인 4, 5, 6, 7, 8각형을 그리는 터틀 그래픽 프로그램

import turtle as t

for i in range(4, 9):       # i가 4부터 8까지 반복될 때
    for j in range(0, i):   # j가 0부터 i번까지
        t.fd(100)           # 앞으로 100픽셀
        t.lt(360/i)         # i각형 만큼 각도에 맞춰 회전

t.done()