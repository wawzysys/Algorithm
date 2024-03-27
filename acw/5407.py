#/E/0Code/Algorithm/acw/5407.py
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
	n, lem = mint()
	def check(n):
		edges = []
		for  t, s in edge:
			if s > n:
				continue 
			l = max(1, t - (n - s))
			r = min(lem, t + (n - s))
			edges.append([l, r])
		edges.sort(key = lambda x : (x[0], x[1]))
		# print(edges)
		n = len(edges)
		if n <= 0:
			return False
		l , r = edges[0]
		for i in range(1, n):
			ll , rr = edges[i]
			if r + 1  >= ll:
				r = max(r, rr)
			else:
				break
		if l <= 1 and r >= lem:
			return True
		return False

	edge = []
	for i in range(n):
		# print(i)
		edge.append(lint())
	l = 0
	mm = 10 ** 10
	r = mm
	while l <= r:
		mid = l + r >> 1
		if check(mid):
			r = mid - 1
		else:
			l = mid + 1
	# print(check(1001))
	print(l)




if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()