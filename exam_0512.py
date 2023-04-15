# 12. 사용자로부터 정수 n을 입력받아서 n각형을 그리는 터틀 그래픽 프로그램

import turtle as t

n = int(input("정수를 입력하시오: "))
print(n, end ="")       # end ="" : 공백 삭제
print("각형을 그립니다.")

for i in range(0, n):
    t.fd(100)           # 앞으로 100
    t.lt(360/n)         # n각 구하기 공식

    # if문 활용
    # if n == 3:
    #     t.fd(100)
    #     t.lt(120)
    # elif n == 4:
    #     t.fd(100)
    #     t.lt(90)
    # elif n == 5:
    #     t.fd(100)
    #     t.lt(72)
    # elif n == 6:
    #     t.fd(100)
    #     t.lt(60)
    # elif n == 7:
    #     t.fd(100)
    #     t.lt(51)

t.done()