# 1. 두 정수를 입력받아서 두 정수 사이의 모든 정수를 더하는 프로그램

num1, num2 = eval(input("두 정수를 입력하시오: "))
sum = 0

for i in range(num1, num2 + 1):     # i가 num1부터 num2 + 1까지
    sum += i                        # sum에 i값 대입

print("두 정수 사이의 모든 정수의 합은", sum, "입니다.")