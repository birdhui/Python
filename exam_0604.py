# 4. 두 수의 사칙계산을 하는 함수 calc_num2(n1, n2, op)를 작성. op의 값이 '+', '-', '*', '/'

def calc_num2(n1, n2, op):
    if (op == '+'):     # op가 +라면
        res = n1 + n2
        return res
    elif (op == '-'):   # op가 -라면
        res = n1 - n2
        return res
    elif (op == '*'):   # op가 *라면
        res = n1 * n2
        return res
    else:               # op가 //라면
        res = n1 // n2
        return res
    
print("calc_num2(2, 3, '+')")
res = calc_num2(2, 3, '+')
print("계산 결과는 ", res, "\n\n")

print("calc_num2(2, 3, '*')")
res = calc_num2(2, 3, '*')
print("계산 결과는 ", res)