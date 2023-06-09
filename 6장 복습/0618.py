def factorial_iter1(n):
    prev = 1

    for i in range(1, n + 1):
        f = i * prev
        prev = f
        return f

print(factorial_iter1(10))