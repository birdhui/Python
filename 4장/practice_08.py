# 답: n3의 값 = 30
n1 = 10
n2 = 20
n3 = 30
mx = 0

# n1이 n2와 값이 같거나 크다면 => False => else문으로 넘어감
if n1 >= n2:
    if n1 >= n3:
        mx = n1
    else:
        mx = n3
# n2가 n3와 값이 같거나 크다면 => False => else의 else문 실행 => mx = n3
else:
    if n2 >= n3:
        mx = n2
    else:
        mx = n3

# n3의 값을 찍음
print(mx)