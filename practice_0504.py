# 5. 다음 작업을 수행하는 코드를 작성하시오.

# 4)
# 실수니까 float, 정수니까 int
rate = float(input("rate의 값을 입력하시오: "))
amount = int(input("amount의 값을 입력하시오: "))

if rate > 0.5 and amount > 500 :
    print("accept")
else :
    print("reject")