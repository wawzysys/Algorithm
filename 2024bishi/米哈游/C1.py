def ksm(a, b, mod):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def solve():
    mod = 10**9 + 7  
    n, q = mint()
    a = [0] + lint()
    cnt = [q] * (n + 1)  
    for i in range(1, q + 1):
        x = sint()
        cnt[x] -= 1
    ans = 0
    for i in range(1, n + 1):
        ans = (ans + a[i] * ksm(2, cnt[i], mod) % mod) % mod
    print(ans)

if __name__ == "__main__":
    solve()
