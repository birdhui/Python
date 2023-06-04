def diffMaxMin(nlist):
    max = nlist[0]
    min = nlist[0]
    res = 0

    for i in nlist:
        if i > max:
            max = i
        elif i < min:
            min = i
    res = max - min
    return res

nlist = [7, 2, 3, 1, 5, 4, 9]
d = diffMaxMin(nlist)
print(d)