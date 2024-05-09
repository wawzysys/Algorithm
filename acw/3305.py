#/E/0Code/Algorithm/acw/3305.py
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
inf = float('inf')
def solve():
	n, m, k, t = mint()
	d = [0] + lint()
	g = defaultdict(list)
	begin = lint()
	vis = set()
	dist = defaultdict(lambda : inf)
	q = deque()
	for x in begin:
		q.append(x)
		vis.add(x)
		dist[x] = 0
	for _ in range(k):
		x, y, target = mint()
		g[x].append((target, max(d[x], d[y]), y))
		g[y].append((target, max(d[x], d[y]), x))
	while q:
		u = q.popleft()
		vis.remove(u)
		if u == t:
			continue
		for j, d, b in g[u]:
			tep = max(dist[u], dist[b]) + d
			if dist[j] > tep:
				dist[j] = tep
				if j not in vis:
					vis.add(j)
					q.append(j)
	print(dist[t])
if __name__ == '__main__':

	solve()