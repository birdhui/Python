# 답: n2
n1 = 3
n2 = 7

if 2 * n1 < n2 and n1 ** 2 < n2:
    print("n1")
else:
    print("n2")

"""
if 조건문 :
    2 * n1 < n2
    2 * n1 = 6
    6 < n2 = True
    and
    n1 ** 2 < n2
    n1 ** 2 = 18
    18 < n2 = False

즉, and 논리연산 조건에 부합하지 않아
else문으로 넘어감
결과값은 n2
"""