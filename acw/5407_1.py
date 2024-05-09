# E:\0Code\Algorithm\acw\5407_1.py 2024-03-30 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

n, len = mint()
a = [lint() for _ in range(n)]

l = 0
r = 10 ** 11 + 7
def check(x):
    temp_a = []
    for idx, t in a:
        if t >x:
            continue
        der = int(x) - t
        l = max(0, idx - der)
        r = min(len, idx + der)
        temp_a.append([l, r])
    # print(temp_a)
    temp_a.sort()
    if not temp_a or temp_a[0][0] > 1:
        return False
    b = [temp_a[0]]
    for l, r in temp_a:
        if b[-1][1] + 1< l:
            return False
        b[-1][1] = max(b[-1][1], r)
    return b[-1][1] >= len
while l <= r:
    mid = l + r >> 1
    if check(mid):
        r = mid - 1
    else:
        l = mid + 1
print(l)

# print(check(10))