#/E/0Code/Algorithm/acw/788.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
# 左闭右闭
class FenWick:
    def __init__(self, n: int):
        self.n = n
        self.tr = [0 for _ in range(n + 1)]

    def sum(self, i: int):
        i += 1
        s = 0
        while i >= 1:
            s += self.tr[i]
            i &= i - 1
        return s

    def rangeSum(self, l: int, r: int):
        return self.sum(r) - self.sum(l - 1)

    def add(self, i: int, val: int):
        i += 1
        while i <= self.n:
            self.tr[i] += val
            i += i & -i
def solve():
    ans = 0
    n = sint()
    a = lint()
    fk = FenWick(10 ** 5 + 10)
    for i, num in enumerate(a):
        fk.add(num, 1)
        ans += i + 1 - fk.rangeSum(1, num)
    print(ans)
if __name__ == '__main__':
    # t = int(input())
    # for _ in range(t):
    #     solve()
    solve()
def kruskal():
    dsu = DSU(n)
    edges.sort(key = lambda x : x[2])
    res = 0
    for u, v, w in edges:
        if dsu.same(u, v):
            continue
        dsu.merge(u, v)
        res += w
    return res if dsu.n == 1 else inf
N = 100010
P = 131
Q = 1 << 64
h = [0]*N
p = [0]*N

def find(l, r):
    return (h[r] - h[l - 1] * p[r - l + 1]) % Q

n,m = map(int,input().split())

s = ' '+ input()

p[0] = 1
for i in range(1,n+1):
    p[i] = p[i - 1] * P % Q
    h[i] = (h[i - 1] * P + ord(s[i])) % Q
    
s = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range (1, m + 1):
        s[i][j] += s[i - 1][j] + a[i][j] + s[i][j - 1] - s[i - 1][j - 1]


for _ in range(q):
    x1, y1, x2, y2 = mint()
    ans = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
    print(ans)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        b[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]
for i in range(q):
    x1, y1, x2, y2, c = mint()
    b[x1][y1] += c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y1] -= c
    b[x2 + 1][y2 + 1] += c
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = b[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        print(a[i][j], end = ' ')
    print()
