# 6. while문을 사용하여 2부터 짝수의 합을 구할 때 그 합이 100이 넘어가는 최초의 짝수를 구하는 프로그램

sum = 0
num = 0

while sum < 100:    # num이 100보다 작을 때
    sum += num      # sum에 num값을 더해가고
    num += 2        # num은 2씩 증가

print("짝수의 합이 100이 넘을 때의 짝수는", num, "입니다.")