# 3. 원의 반지름과 원주율을 입력받아서 원의 넓이를 구하는 함수 area_circle(r, pi)를 작성

# 원의 넓이 구하는 함수 정의
def area_circle(r, pi=3.14):    # 디폴트 인수를 사용해 인수가 없는 경우 계산
    circle = pi * r * r
    return circle

circle = area_circle(2, 3.14159)
print("area_circle(2, 3.14159)")
print("원의 면적은 ", float(circle), "\n\n")

circle = area_circle(3)
print("area_circle(3)")
print("원의 면적은 ", round(circle, 2))     # round() 함수를 사용해 소수점 지정하는 방법