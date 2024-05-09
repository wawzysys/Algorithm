#/E/0Code/Algorithm/acw/蓝桥杯/4957.py
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
	N = sint()
	# print(N)
	g = [lint() for _ in range(N)]
	for i in range(N):
		g[i][1] += g[i][0]
	# print(g)
	st = [0] * (N)
	ans = [0]
	def dfs(u, last):
		# print("u", u, st, last)
		if u == N:
			ans[0] = 1
			return 
		lastCopy = last
		for i in range(N):
			if st[i] == 1:
				continue
			if g[i][1] < last:
				continue
			st[i] = 1
			dfs(u + 1, max(g[i][0], last) + g[i][2])
			st[i] = 0

	
	dfs(0, -1)

	if ans[0] == 1:
		print("YES")
	else:
		print("NO")



if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	  solve()

	# solve()