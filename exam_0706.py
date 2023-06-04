def sumMat(mat):
    res = 0
    for i in mat:
        res += sum(i)
    return res

mat = [[1, 1],[2, 2],[1, 1]]
hap = sumMat(mat)
print(hap)