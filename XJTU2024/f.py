# E:\0Code\Algorithm\XJTU2024\f.py 2024-05-21 by 777
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
    cnt = defaultdict(int)
    n, m = mint()
    a = lint()
    for i, c in enumerate(a):
        cnt[c] += i + 1
    for _ in range(m):
        x, y = mint()
        print(cnt[x]*cnt[y])
    








if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()