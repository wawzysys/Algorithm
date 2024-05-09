# E:\0Code\Algorithm\acw\1343.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a = []
for i in range(n):
    a.append(lint())
a.sort()
b = []
ans1 = 0
ans2 = 0
for l, r in a:
    if not  b or b[-1][1] < l:
        if b:
            ans2  =max(ans2, l - b[-1][1])
        b.append([l, r])
    else:
        b[-1][1] = max(b[-1][1], r)
for l, r in b:
    ans1 = max(ans1, r - l)
print(ans1, ans2)