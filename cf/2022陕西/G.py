def f(n):
    if n % 2 == 1:
        return (n - 1) // 2 * (n - 1) // 2
    return n // 2 * (n - 2) // 2

n, m = map(int, input().split())
if f(n) >= m:
    print(f(n))
else:
    l = 1
    r = 10 ** 10
    while l <= r:
        mid = (l + r) >> 1
        if f(mid) >= m:
            r = mid - 1
        else:
            l  = mid + 1
    print(l)