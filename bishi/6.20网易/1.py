# E:\0Code\Algorithm\bishi\6.20网易\1.py 2024-06-20 by 777
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
    a = lint()
    b = lint()
    c = lint()
    d = lint()
    op = 0
    idx1 = 0
    idx2 = 0
    while idx1 < 5 and idx2 < 5:
        if op % 2 == 0:
            d[idx2] -= a[idx1]
            if d[idx2] <= 0:
                idx2 += 1
        else:
            b[idx1] -= c[idx2]
            if b[idx1] <= 0:
                idx1 += 1
        op += 1
    if idx1 < 5:
        ans = 5 - idx1
        result = "win"
    else:
        ans = 5 - idx2
        result = "lose"
    print(result)
    print(ans)

if __name__ == '__main__':
    solve()