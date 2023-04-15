# 2. 다음 리스트 중에서 10보다 작은 수를 모두 더하여 출력하는 프로그램

nlist = [4, 12, 7, 1, 9, 15]
sum = 0

for i in range(0, 6):       # i가 0부터 6까지 1씩 증가
    if(nlist[i] < 10):      # nlist[i]가 10보다 작다면
        sum += nlist[i]     # sum에 대입

print("10보다 작은 수의 합은", sum, "입니다.")