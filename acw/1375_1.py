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
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def spfa(u, n, g) -> int:
	q = deque()
	q.append(u)
	vis = set()
	dist = defaultdict(lambda : inf)
	vis.add(u)
	dist[u] = 0
	while q:
		t = q.popleft()
		vis.remove(t)
		for j, d in g[t]:
			if dist[j] > dist[t] + d:
				dist[j] = dist[t] + d
				if j not in vis:
					vis.add(j)
					q.append(j)
	return dist[n]

def solve():
	n = sint()
	g = defaultdict(list)
	begin = set()
	for _ in range(n):
		x, y, z = input().split()
		z = int(z)
		g[x].append((y, z))
		g[y].append((x, z))
		begin.add(x)
		begin.add(y)
	ans_d = inf
	ans = -1
	for x in begin:
		if 'A' <= x < 'Z':
			tep = spfa(x, g)
			# print(tep)
			if tep < ans_d:
				ans_d = tep
				ans = x
	print(ans,ans_d)








if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()