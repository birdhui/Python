nlist = [2, 5, 8, 3]

def find_list(nlist, n):
    if n in nlist:
        return True
    else:
        return False

res = find_list(nlist, 3)
print(res)