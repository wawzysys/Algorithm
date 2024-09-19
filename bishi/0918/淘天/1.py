MOD = 10**9 + 7
PHI = MOD - 1  

def f(n, m):
    if n < 2 or m < 2:
        return 0

    t1 = (n - 1) % MOD
    t2 = (m - 1) % MOD

    nm_mod = (n % PHI) * (m % PHI) % PHI
    x = (nm_mod - 4) % PHI

    power = pow(26, x, MOD)

    res = 588 * t1 % MOD
    res = res * t2 % MOD
    res = res * power % MOD

    return res

n, m = map(int, input().split())
print(f(n, m))
