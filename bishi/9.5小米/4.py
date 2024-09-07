import math
n, k = map(int, input().split())
if n % 2 == 1:
    print(0)
else:
    mod = 908244353
    n = n // 2

    c = math.comb(2 * n, n) // (n + 1)

    result = c * pow(k, n, mod)

    print(result % mod)


