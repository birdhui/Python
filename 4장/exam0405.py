n1, n2, n3 = eval(input("세 정수를 입력하시오: "))

# 첫 번째 : min함수 사용
print("가장 작은 수는", min(n1, n2, n3), "입니다.")

# 두 번째 : if문 사용
temp = 0

if n1 < n2:
    temp = n1
    if n2 < temp:
        temp = n2
    if n3 < temp:
        temp = n3

print("가장 작은 수는", temp, "입니다.")

# 세 번째 : 삼항 연산자 사용
min = 0

min = (n1 if n1 > n2 else n2) if ((n1 if n1 < n2 else n2) < n3) else n3
print("가장 작은 수는", min, "입니다.")