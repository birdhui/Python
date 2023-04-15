# 4. 다음 문장에 맞는 if 조건문을 작성하세요.

height, age, price, tax, year = eval(input("height, age, price, year 순으로 값을 입력하시오:"))
# height = 180
# age = 18
# price = 900
# tax = 9
# year = 1900

if height >= 170 :
    print("height가 170보다 크거나 같습니다.")
    if age > 10 and age < 19 :
        print("age가 10보다 크고 19보다 작습니다.")
        if price < 1000 or tax < 10 :
            print("price가 1000보다 작거나 tax 값이 10보다 작습니다.")
            if year < 2000 and year % 5 == 0 :
                print("year이 2000보다 작고 5의 배수입니다.")
else :
    print("조건문을 만족시키지 못합니다.")