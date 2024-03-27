#/E/0Code/Algorithm/acw/851.py
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
	N = n + 5
	g = [[] for _ in range(N)]
	dist = [inf] * N
	st = [False] * N
	q = deque()
	
	for i in range(m):
		x, y, d = mint()
		g[x].append((y, d))

	q.append(1)
	dist[1] = 0
	st[1] = True

	while(q):
		t = q.popleft()
		st[t] = False
		for j, d in g[t]:
			if dist[j] > dist[t] + d:
				dist[j] = dist[t] + d
				if not st[j]:
					st[j] = True
					q.append(j)

	if dist[n] == inf:
		print("impossible")
	else:
		print(dist[n])
	
 
if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()