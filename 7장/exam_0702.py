def divide3(nlist):
    n0 =[]
    n1 =[]
    n2 =[]

    for i in nlist:
        if i % 3 == 0:
            n0.append(i)
        elif i % 3 == 1:
            n1.append(i)
        else:
            n2.append(i)
    return n0, n1, n2
    
nlist = [1, 2, 3, 4, 5, 6, 7, 8]
n0, n1, n2 = divide3(nlist)
print("n0=", n0)
print("n1=", n1)
print("n2=", n2)