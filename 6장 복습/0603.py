def calcCircum(radius):
    c = 3.14 * radius * 2
    return c

radius = int(input("반지름을 입력하시오:"))
circum = calcCircum(radius)
print("원주 =", circum)