#/E/0Code/Algorithm/acw/蓝桥杯/4407.py
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
	g1 = [lint() for _ in range(n)]
	g2 = [lint() for _ in range(m)]
	graph = defaultdict(int)
	cnt = defaultdict(int)
	for x, y, d in g1:
		cnt[(x, y)] += 1
		graph[(x, y)] = max(graph[(x, y)], d)
	for x, y, d in g2:
		graph[(x, y)] = max(graph[(x, y)], d)
	ans = 0
	for x, y, d in g2 :
		q = deque()
		q.append((x,y))
		while q:
			(x, y) = q.popleft()
			ans += cnt[(x, y)]
			d = graph[(x, y)]
			del graph[(x, y)], cnt[(x, y)]
			for i in range(x - d, x + d + 1):
				for j in range(y - d, y + d + 1):
					if (i - x) ** 2 + (j - y) ** 2 <= d ** 2 + 1e-6 :
						if (i, j) in graph:
							q.append((i, j))
	print(ans)



		






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()