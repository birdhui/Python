# 1. 두 수를 입력받아서 두 수의 차이를 반환하는 함수 diff2

num1, num2 = eval(input("두 수를 입력하시오 (예:2,5) : "))

def diff2(n1, n2):      # 두 수의 차이가 항상 양수가 되기 위해서는
    if (n1 > n2):       # n1이 n2보다 크다면
        return n1 - n2  # n1에서 n2를 빼기
    else:               # n2가 n1보다 크다면
        return n2 - n1  # n2에서 n1을 빼기

res = diff2(num1, num2) # 변수 res에 diff2함수 값 대입
print("두 수의 차이는 ", res)   # 값 출력