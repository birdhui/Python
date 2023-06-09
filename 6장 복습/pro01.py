def diff2(n1, n2):
    if (n1 > n2):
        num = n1 - n2
    else:
        num = n2 - n1
    return num

n1, n2 = eval(input("두 수를 입력하시오 (예: 2,5) :"))
print("두 수의 차이는", diff2(n1, n2))