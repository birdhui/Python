# 7. 영어 문장을 입력 받아서 알파벳 'a'의 개수를 출력하는 프로그램

eng = (input("영어 문장을 입력하시오: "))       # 문자열로 입력받기
count = 0

for i in range(len(eng)):                     # i가 입력받은 eng의 길이만큼
    ch = eng[i]                               # ch에 i값을 대입
    if ch == 'a':                             # 만약, ch가 'a'와 같다면
        count += 1                            # count를 1씩 증가

print("'a'의 개수는", count, "개입니다.")