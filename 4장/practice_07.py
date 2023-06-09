# 답: 3번, 4번
year = 2020
month = 2

# 1)
# year이 2000보다 크고 month가 2보다 작다면 => "late"
if year > 2000 and month < 2:
    print("early")
else:
    print("late")

# 2)
# year이 2000보다 크거나 month가 6보다 작다면 => "late"
if year > 2000 or month < 6:
    print("late")
else:
    print("early")

# 3)
# year이 2000보다 크다면, month가 2보다 작다면 => "early"
if year > 2000:
    if month < 6:
        print("early")
else:
    print("late")

# 4)
if year > 2000 and month < 6:
    print("early")   # 큰따옴표로 제대로 묶이지 않아 출력되지 않았음 -> 문제지 오타 => 오타가 아니라면 답은 2개가 아니라 1개임
else:
    print("late")