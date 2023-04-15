# 10. while문을 사용하여서 입력한 수의 제곱을 출력하고 음수가 입력되면 while루프를 종료하는 프로그램

num = 1

while num >= 0:                                 # num이 0보다 크거나 같다면
    num = int(input("정수를 입력하시오: "))      # 반복해서 사용자로부터 입력받기
    if num > 0:                                 # 만약, num이 0보다 크다면
        print("제곱은", num * num, " ")         # num의 제곱값 출력
    else:
        print("종료합니다.")