
#/E/0Code/Algorithm/bishi/baidu/2.py
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
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    
    n, m = map(int, input().split(','))
    ans = 0
    for i in range(n, m + 1):
        if i % 2 == 0 and  i % 3 == 0:
            ans += i
    print(ans)

if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()