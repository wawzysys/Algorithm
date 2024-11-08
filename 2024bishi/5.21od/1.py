from functools import cache
import sys
sys.setrecursionlimit(100000)
m, n = map(int, input().split())

@cache
def solve(l, low, high, remain):
    if l == m - 1:
        if remain - low <= 3:
            return 1
        return 0
    ans = 0
    for i in range(low, high + 1):
        remain -= i
        if remain // (m - l - 1) < i:
            break
        ans += solve(l + 1, i, min(i + 3, remain // (m - l - 1)), remain)
        remain += i
    return ans

if m == 1:
    print(1)
else:
    ans = solve(0, 1, n // m, n)
    print(ans)


