# 정수를 입력받아서 100보다 크고 짝수인지 확인하는 프로그램
num = int(input("정수를 입력하시오: "))
print(num > 100 and num % 2 == 0)       # num값을 2로 나눈 나머지가 0이면 짝수