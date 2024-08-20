import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
N = 1010
M = 1000010
n = 0
a = [0 for _ in range(N)]
use = [False for _ in range(M)]
b = [0 for _ in range(N)]
def solve(x):
    nihao = 0;
    for i in range(1, n + 1):
        if (a[i] != x):
            nihao += 1
            b[nihao] = a[i]
    ans = 0
    ll = 1
    kk = 1
    while(ll <= nihao):
        while (kk < nihao and b[kk + 1] == b[ll]):
            kk+= 1
        ans = max(ans, kk - ll + 1);
        kk = kk + 1
        ll = kk
    return ans;

n = sint()
for i in range(1, n + 1): 
    a[i] = sint()
    use[a[i]] = True

ans1 = 0
ll = 1
kk = 1
while (ll <= n):
    while(kk < n and a[kk + 1] == a[ll]):
        kk += 1
    ans1 = max(ans1, kk - ll + 1);
    # print(ans1)
    kk += 1
    ll = kk
ans2 = 0;
for i in range(1, M - 10):
    if (use[i]):
        ans2 = max(ans2, solve(i))
print(ans2 - ans1 )
