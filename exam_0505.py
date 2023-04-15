# 5. 정수를 입력하면 그 정수의 모든 약수를 출력하는 프로그램

num = int(input("정수를 입력하시오: "))

for i in range(1, num + 1, 1):  # i가 1부터 num까지 1씩 증가
    if(num % i == 0):           # 만약, i를 num으로 나눈 나머지가 0일 때
        print(i, end = " ")     # i값 출력 / i = num의 약수