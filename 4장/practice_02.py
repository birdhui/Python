# 다음 if 조건문의 문법에 유의하여 옳은 걸을 모두 고르시오.
# 답 : 1번, 3번, 4번

# 1) - 맞음
a = 3

if a > 0 :
    print("a는 양수입니다.")

# 2) - 틀림 (나머지가 1이기 때문에 홀수임)
num = 5

if num % 2 == 0 :
    print("num은 짝수입니다.")

# 3) - 맞음
msg = "hello"

if len(msg) > 0:
    print("msg의 길이는 0보다 큽니다.")

# 4) - 맞음 (n이 10보다 작기 때문에 대입연산자를 이용해 m값을 1 증가시킴)
n = 7
m = 5

if n < 10:
    m += 1
    print("m의 값을 1 증가하였습니다.")