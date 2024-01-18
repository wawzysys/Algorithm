
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n = sint()
	w = []
	vis = [0 for _ in range(n)] 
	for _ in range(n):
		w.append(sint())
	# print(w)
	g = [[] for _ in range(n)]
	for _ in range(n - 1):
		a, b = mint()
		g[b - 1].append(a - 1)
		vis[a - 1] += 1
	# print(g)
	#找到根节点
	root = -1
	for i in range(n):
		if vis[i] == 0:
			root = i
			break

	ans = 0
	def dfs(x):
		x_yes, x_no = w[x], 0
		for j in g[x]:
			j_yes, j_no = dfs(j)
			x_yes += j_no
			x_no += max(j_yes,j_no)
		nonlocal ans
		ans = max(ans, x_no, x_yes)
		return x_yes, x_no
	dfs(root)
	print(ans)

if __name__ == '__main__':
    solve()
