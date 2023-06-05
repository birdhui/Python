# 근의 판별식 b2-4ac의 값이 양수이면 1을 반환, 음수이면 -1을 반환, 0일 때는 0을 반환하는 함수 root_det(a, b, c)

def root_det(a, b, c) :
    res = (b**2) - (4*a*c)  # 근의 판별식 변수에 대입

    if res > 0:             # res 값이 0보다 큰 양수라면
        return 1            # 1을 반환
    elif res == 0:          # 0과 같다면
        return 0            # 0을 반환
    else:                   # 음수라면
        return -1           # -1을 반환

det = root_det(2, 3, 1)
print("판별식 값: ", det)
