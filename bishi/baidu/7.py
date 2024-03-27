#/E/0Code/Algorithm/bishi/baidu/7.py
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
	n, m = mint()
	g = defaultdict(list)
	for i in range(m):
		x, y = mint()
		g[x].append(y)
	vis = set()
	vis.add(1)
	def dfs(x):
		for j in g[x]:
			if j not in vis:
				vis.add(j)
				dfs(j)
	dfs(1)
	if n in vis:
		print("Yes")
	else:
		print("No")


if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()