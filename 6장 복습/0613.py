def addNums(*nums):
    hap = 0
    for n in nums:
        hap += n
    return hap

hap1 = addNums(1, 2)
print(hap1)

hap2 = addNums(1, 2, 3, 4)
print(hap2)