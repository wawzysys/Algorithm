# E:\0Code\Algorithm\bishi\4.18高德\a.py 2024-04-18 by 777
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
from bisect import*
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    N = int(input())
    a = list(map(int, input().split()))
    r = max(a) * n * n
    l = 0
    def check(x):
        ans = 0
        for num in a:
            ans += int((x // num) ** (0.5))
        return ans >= n
    
    # print(bisect_right(range(10000000000), True, n, key=check))
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1    
    print(l)
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        solve()

    # solve()