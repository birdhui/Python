def calc_num2(n1, n2, op):
    if(op == '+'):
        res = n1 + n2
    elif(op == '-'):
        res = n1 - n2
    else:
        res = n1 * n2
    return res

res = calc_num2(2, 3, '*')
print("계산 결과는", res)