#/E/0Code/Algorithm/bishi/4.12饿了么/2.cpp
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
	n, m = mint()
	a = [0] + lint()
	print(a)
	sum = [[0 for i in range(n + 10)] for j in range(5)]
	for i in range(1, n + 1):
		for j in range(5):
			sum[j][i] += sum[j][i - 1] + (a[i] >> j & 1)
	# print(sum)
	def get(l, r):
		x = 0
		for i in range(5):
			if sum[i][r] - sum[i][l - 1] > 0:
				x += 1 << i
		return x
	for _ in range(m):
		l, r, k = mint()
		t = l
		t_r = r
		while l <= r:
			mid = (l + r) // 2
			if get(t, mid) >= k:
				r = mid - 1
			else:
				l = mid + 1
		if get(t, l) == k and l <= t_r :
			print(l)
		else:
			print(-1)
if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()