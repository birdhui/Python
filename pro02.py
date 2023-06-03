n1, n2 = eval(input("큰 정수와 작은 정수를 입력하시오 (예: 4,3) :"))

def quot_div(n1, n2):
    p1 = n1 // n2
    p2 = n1 % n2
    return p1, p2

n1, n2 = quot_div(n1, n2)
print("몫과 나머지는", n1, n2)