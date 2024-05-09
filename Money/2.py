#/E/0Code/Algorithm/OJ/2.py
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
    n = int(input())
    ans = defaultdict(list)
    mm = float('inf')
    high = []
    for _ in range(n):
        a = sint()
        high.append(a)
    for i in high:
        ss = 0
        for j in high:
            ss += abs(i - j)
        if ss <= mm:
            ans[ss].append(i)
            mm = ss
    res = float('-inf')
    for j in ans[mm]:
        res = max(j, res)
    print(res)


if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()