#/E/0Code/Algorithm/acw/1375_1.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def solve():
	n, m = mint()
	g = defaultdict(list)
	for _ in range(m):
		x, y, z = mint()
		g[x].append((y, z))
	q = [(0, 1)] # 距离 顶点
	vis = set()
	dist = defaultdict(lambda : inf)
	dist[1] = 0
	while q:
		d, u = heappop(q)
		if u in vis:
			continue
		vis.add(u)
		for j, d in g[u]:
			if j not in vis and dist[j] > dist[u] + d:
				dist[j] = dist[u] + d
				heappush(q, (dist[j], j))
	# return dist[n]
	print(dist[n]) if dist[n] != inf else print(-1)
if __name__ == '__main__':
	solve()