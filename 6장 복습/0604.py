def calcAvg(nlist):
    avg = 0
    for num in nlist:
        avg += num
        avg = avg / len(nlist)
        return avg
    
nlist = [1, 3, 5, 8, 9]
avg = calcAvg(nlist)
print("평균 =", avg)