def get_hap_diff(a, b):
    hap = a + b
    diff = a - b if a > b  else b - a
    return hap, diff

a = 3
b = 5
hap, diff = get_hap_diff(a, b)
print("합 =", hap, "차 =", diff)