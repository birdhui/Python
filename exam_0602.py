# 2. 큰 정수와 작은 정수를 입력받아서 두 수의 몫과 나머지를 구하는 함수 quot_div(n1, n2)를 작성. (몫과 나머지 두 개를 반환하도록)

num1, num2 = eval(input("큰 정수와 작은 정수를 입력하시오 (예:4,3) : "))

# quot_div 함수 정의
def quot_div(n1, n2):
    quot = n1 // n2                  # n1 / n2 (몫)
    rem = n1 % n2                    # n1 % n2 (나머지)
    return quot, rem                 # tuple로 두 개의 반환값을 지정

res1, res2 = quot_div(num1, num2)    # 튜플의 unpack 기능을 이용해 변수 2개에 각각 값을 받기
print("몫과 나머지는", res1, res2)
