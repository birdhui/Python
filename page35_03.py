# 아기의 태어난 개월 수를 입력하면 몇 년 몇 개월로 바꿔 주는 프로그램
months = int(input("태어난 개월 수를 입력하시오: "))
# 태어난 개월 수를 12로 나눠 년수를 구함
babyYear = months / 12
# 태어난 개월 수를 12로 나눈 나머지값을 변수에 대입
babyMonths = months % 12
print("%d년 %d개월" % (babyYear, babyMonths))