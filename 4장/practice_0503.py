# 5. 다음 작업을 수행하는 코드를 작성하시오.

# 3)
x = int (input("x의 값을 입력하시오: "))
y = int (input("x의 값을 입력하시오: "))

# x가 y보다 크다면
if x > y :
    # 변수 diff에 x - y를 계산해 저장
    diff = x - y
    print("diff =", diff)
# y가 x보다 크다면
elif y > x :
    # 변수 diff에 y - x를 계산해 저장
    diff = y - x
    print("diff =", diff)