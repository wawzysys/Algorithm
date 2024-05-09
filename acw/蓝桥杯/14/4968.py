def fun(n: int) -> int:
    res, i = n, 2
    while i ** 2 <= n:
        if n % i == 0:
            res = res * (i - 1) // i
            while n % i == 0:
                n //= i
        i += 1
    return res if n == 1 else res * (n - 1) // n

a, b = map(int, input().split())
MOD = 998244353
print(0 if a == 1 else pow(a, b - 1, MOD) * fun(a) % MOD)
