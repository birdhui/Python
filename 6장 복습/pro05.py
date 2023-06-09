def avg_list(nlist):
    res = sum(nlist) / len(nlist)
    return res

nlist = [2, 5, 8, 3]
avg = avg_list(nlist)
print("평균=", avg)