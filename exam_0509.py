# 9. for문을 사용하여서 1부터 100까지의 정수를 출력하되 3의 배수는 건너뛰는 프로그램

num = 0

for i in range(1, 11):              # i가 1부터 10까지
    if i % 3 == 0:                  # 3의 배수면 다음 코드로
        continue
    else:
        if i != 10:                 # 만약, i가 10이라면
            print(i, end = ", ")    # 10 제외하고 출력
        else:                       # 10이라면
            print(i)                # 10 출력
