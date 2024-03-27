import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
n, m = mint()
N = n + 5
g = [[inf for i in range(N)] for j in range(N)]
g[1][1] = 0
for i in range(m):
	a, b, c = mint()
	g[a][b] = min(g[a][b], c)
	g[b][a] = min(g[b][a], c)
for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			g[i][j] = min(g[i][j], g[i][k] + g[k][j])
mm = 0
for i in range(1, n + 1):
	if g[1][i] == inf:
		print(-1)
		break
	else:
		mm = max(g[1][i], mm)
print(mm)
