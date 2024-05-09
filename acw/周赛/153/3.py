# E:\0Code\Algorithm\acw\周赛\153\3.py 2024-04-27 by 777
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
from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
# import math
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = sint()
    a = lint()
    b = lint()
    inf = float('inf')
    ans = inf 
    for c, v in zip(a, b):
        if c == 1:
            ans = min(ans, v)
    for i, num1 in enumerate(a):
        for j, num2 in enumerate(a):
            if i == j:
                continue
            if gcd(num1, num2) == 1:
                ans = min(ans, b[i] + b[j])
    if ans == inf:
        print(-1)
    else:
        print(ans)

        






if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()