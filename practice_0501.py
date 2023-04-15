# 5. 다음 작업을 수행하는 코드를 작성하시오.

# 1)
degree = int(input("degree 값을 입력하시오(0~30 사이): "))

if degree > 30 :
    print("hot")
elif degree >= 10 and degree <= 19 :
    print("mild")
elif degree >= 20 and degree <= 30 :
    print("warm")
else :
    print("cold")