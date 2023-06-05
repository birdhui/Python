def common(list1, list2):
    list = list1[0]
    for i in list1:
        if i in list2:
            return True
        else:
            return False

list1 = [3, 7, 9, 11, 15]
list2 = [2, 3, 5]
print(common(list1, list2))