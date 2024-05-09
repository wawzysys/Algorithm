
# E:\0Code\Algorithm\acw\803.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a = [lint() for _ in range(n)]
a.sort()
last = a[0][1]
ans = 1
for l, r in a[1:]:
    if l > last:
        ans += 1
    last = max(last, r)
print(ans)