def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <=n // i:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(1, 2025):
    if 2024 % i == 0 and is_prime(i):
        print(i, end=' ')
