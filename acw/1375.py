#/E/0Code/Algorithm/acw/1375.py
import sys
input=lambda:sys.stdin.readline().strip()
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

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
	ans = 0
	for x in begin:
		if 'A' <= x < 'Z':
			q = deque([x])
			vis = set([x])
			dist = defaultdict(lambda : inf)
			dist[x] = 0
			while q:
				t = q.popleft()
				vis.remove(t)
				for j, d in g[t]:
					if dist[j] > dist[t] + d:
						dist[j] = dist[t] + d
						if j not in vis:
							vis.add(j)
							q.append(j)
			if dist['Z'] < ans_d:
				ans_d = dist['Z']
				ans = x
	print(ans, ans_d)





if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()