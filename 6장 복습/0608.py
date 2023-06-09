def isPrime(num):
    for n in range(2, int(num/2) + 1):
        if num % n == 0:
            return False
        return True

num = int(input("정수를 입력하시오:"))
if isPrime(num) == True:
    print(num, "은 소수입니다.")
else:
    print(num, "은 소수가 아닙니다.")