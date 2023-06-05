def psum(nlist, i1, i2):
    sum = 0
    for i in range(i1, i2+1):
        sum += nlist[i]
    return sum

nlist = [7, 2, 3, 1, 5, 4, 9]
hap = psum(nlist, 1, 3)
print("부분합은", hap, "입니다.")