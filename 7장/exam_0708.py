def maxRow(mat):
    max_values = []
    for row in mat:
        max_value = max(row)
        max_values.append(max_value)
    return max_values

mat = [[1,3,1],[7,2,1],[0,3,5]]
mlist = maxRow(mat)
print(mlist)