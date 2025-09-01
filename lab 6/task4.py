def sum_to_n(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
print(sum_to_n(10))