def area_circle(r, pi=3.14):
    # 디폴트 인수 사용!!
    if (pi > 0):
        res = pi * r * r
    else:
        res = pi * r * r
    return res

area = area_circle(3)
print("원의 면적은", area)