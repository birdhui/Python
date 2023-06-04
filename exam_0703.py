def word3(list):
    str = list[0]
    cnt = 0
    for i in range(len(str)):
        if len(list[i]) == 3:
            cnt = cnt + 1
    return cnt

wlist = ["bag", "computer", "pen", "happy", "book"]
cnt = word3(wlist)
print(cnt)