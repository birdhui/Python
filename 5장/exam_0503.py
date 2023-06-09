# 3. 다음 리스트 중에서 짝수 인덱스의 원소들만을 출력하는 프로그램

nlist = [2, 3, 7, 4, 9, 5]
num = 0

for i in range(len(nlist)):     # i가 배열 인덱스의 길이만큼
    if(i % 2 == 0):             # i를 2로 나눈 값이 0일 때
        num = nlist[i]          # num에 배열[i] 값 대입
        print(num)