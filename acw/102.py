#/E/0Code/Algorithm/acw/102.py
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
	n, f = mint()
	a = [0] + [sint() for i in range(n)]
	def check(avg):
		s = [0] * (n + 10)
		for i in range(1, n + 1):
			s[i] = s[i - 1] + a[i] - avg
		minv = inf
		ans = -inf
		for i in range(f, n + 1):
			minv = min(s[i - f], minv)
			ans  = max(ans, float(s[i] - minv))
		if ans >= 0:
			return True
		else:
			return False
	l = 0 
	r = 10 ** 10
	while r > l + 1e-5:
		mid = (l + r) / 2
		if check(mid):
			l = mid
		else:
			r = mid
	print(int(r * 1000))
if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()