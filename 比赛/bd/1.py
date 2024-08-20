
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
n = sint()
a = lint()
b = lint()
x, y, c = mint()
def check(xx):
    ans = 0
    for i, num  in enumerate(b):
        tep = num
        if x > num:
            tep = ((x - num - 1) // a[i] + 1) * a[i] + num
        if xx >= tep:
            ans = ans + (xx - tep) // a[i] + 1
        if ans >= c:
            return True
    return False

l = x
r = y
while  l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
if check(l):
    print(l)
else:
    print(-1)
