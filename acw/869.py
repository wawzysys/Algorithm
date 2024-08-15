#/E/0Code/Algorithm/acw/869.py
import sys

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()
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
    n = sint()
    for _ in range(n):
        a = sint()
        ans = set()
        i = 1
        while i * i <= a:
            if a % i == 0:
                ans.add(i)
                ans.add(a // i)
            i += 1
        print(*sorted(ans))


if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()
