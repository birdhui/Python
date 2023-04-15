# 8. 주사위를 100번 던져서 1의 눈이 나오는 횟수를 시뮬레이션하는 프로그램

import random

cnt = 0

for i in range(100):            # 0부터 100까지
    num = random.randint(1, 6)  # 1부터 6까지
    i = num                     # i에 num값 대입
    if i == 1:                  # 만약, i가 1이라면
        cnt += 1                # cnt 1씩 증가

print("1의 눈이 나온 횟수는", cnt, "번입니다.")