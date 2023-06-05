def addMatrix(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            mat1[i][j] += mat2[i][j]
    return mat1

mat1 = [[1,1,1],[2,2,2],[3,3,3]]
mat2 = [[2,2,2],[0,0,0],[3,3,3]]

m = addMatrix(mat1, mat2)
print(m)