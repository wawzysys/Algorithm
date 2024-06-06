# E:\0Code\Algorithm\代码源\倍增\1.py 2024-05-31 by 777
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

def solve():
    inf = float("inf")
    n,m=mint()
    a=[0] + lint()
    N = 10**5 + 11
    f = [[0 for _ in range(21)] for _ in range(N)]
    v = [inf for _ in range(N)]
    c = [[]for _ in range(N)]
    st = set()
    for i in range(2, 10**5 + 1):
        if i in st: continue
        c[i].append(i)
        for j in range(i * 2, 10**5 + 1, i):
            st.add(j)
            c[j].append(i)
    f[n + 1][0] = n + 1
    for i in range (n, 0, -1):
        f[i][0] = f[i + 1][0]
        for j in c[a[i]]:
            f[i][0] = min(f[i][0], v[j])
            v[j] = i
    for i in range(1, 21):
        for j in range(1, n + 1):
            if f[j][i - 1] <= n:
                f[j][i] = f[f[j][i - 1]][i - 1]
            else:
                f[j][i] = n + 1
    for _ in range(m):
        l, r = mint()
        ans = 0
        for i in range(20, -1, -1):
            if f[l][i] <= r:
                ans += 1 << i
                l = f[l][i]
        ans += 1
        print(ans)






if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()