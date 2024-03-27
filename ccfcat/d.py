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
import copy
n, m = mint()
grid = []
cnt = defaultdict(int)
for i in range(m):
	a = lint()
	grid.append(a)
for i in range(n):
	for j in range (m):
		cnt[grid[i][j]] += 1
mm = 0
for k, v in cnt.items():
	mm = max(v, mm)
if mm < 3:
	print(0)
grid_copy = copy.deepcopy(grid)#用来记录是否访问过
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs1(i, j, pre):
	if i < 0 or i >= n or j < 0 or j >= m or grid_copy[i][j] == 0 or grid[i][j] != pre:
		return
	grid_copy[i][j] = 0 #标记为访问过
	ans = 1
	for k in range(4):
		ans += dfs1(i + dx[k], j + dy[k], pre)
	return ans
def check():
	ans = 0
	for i in range(n):
		for j in range(m):
			ans = dfs1(i, j, grid[i][j])
			if ans > 3:
				return True
	return False
			
def dfs2(i, j):
	if check():
		return
	ans = 0

	ans += dfs1(i, j, grid[i][j])
	

for i in range(i):
	for j in range(j):
