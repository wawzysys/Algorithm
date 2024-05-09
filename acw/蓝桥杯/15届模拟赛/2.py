# E:\0Code\Algorithm\acw\蓝桥杯\15届模拟赛\2.py 2024-04-12 by 777
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
    s = list(input())
    n = len(s)
    flag = 0
    ans = []
    for c in s:
        if c == 'L' and flag == 1:
            continue
        if c == 'Q':
            flag = 0
        if c == 'L':
            flag = 1
        ans.append(c)
    print("".join(ans))
        
        
        






if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()