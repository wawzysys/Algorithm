# E:\0Code\Algorithm\acw\422.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
L, m = mint()
a = [lint() for _ in range(m)]
a.sort()
b = []
ans = 0
for l, r in a:
    if not b or l > b[-1][1]:
        b.append([l, r])
    else:
        b[-1][1] = max(b[-1][1], r)
        
for l, r in b:
    ans += r - l + 1
print(L + 1 - ans)