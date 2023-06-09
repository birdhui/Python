def my_divmod(n1, n2):
    quot = n1 // n2
    rem = n1 % n2
    return (quot, rem)

quot, rem = my_divmod(10, 3)
print(quot, rem)