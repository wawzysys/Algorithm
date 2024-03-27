#/E/0Code/Algorithm/acw/562.py
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

def solve(tt):
	n = sint()
	s = input()
	a = [0]
	for c in s:
		a.append(int(c))
	for i in range(1, n + 1):
		a[i] += a[i - 1] 
	Len = (n + 1)// 2
	mmax = -inf
	for i in range(Len, n + 1):
		mmax =  max(mmax, a[i] - a[i - Len])
	print("Case #{t}: {mmax}".format(t = tt + 1, mmax = mmax))
	# print(mmax)
if __name__ == '__main__':
	t=int(input())
	# s = [0] * (5 * (10 ** 6) + 10)
	for tt in range(t):
	  solve(tt)

	# solve()