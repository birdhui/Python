# 5. 다음 작업을 수행하는 코드를 작성하시오.

# 2)
age = int(input("age값을 입력하시오(0~100 사이): "))
fare = 0

# age가 60보다 크다면
if age > 60 :
    fare = 3000
    print("fare의 값은", fare)

# age가 20과 같거나 크거나 60과 작거나 같거나
elif age >= 20 and age <= 60 :
    fare = 5000
    print("fare의 값은", fare)

# age가 20보다 작다면
elif age < 20 :
    fare = 2000
    print("fare의 값은", fare)