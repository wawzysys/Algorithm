
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	t = sint()
	for _ in range(t):
		n = sint()
		color = [-1] + list(input())
		g = [[] for _ in range(n + 1)]
		for _ in range(n - 1):
			a, b = mint()
			g[a].append(b)
			g[b].append(a)
		ans = 0
		def dfs(x, fa):
			nonlocal ans
			x_len = 0
			for j in g[x]:
				if j == fa:
					continue
				j_len = dfs(j, x)
				if color[j] == color[x]:
					ans = max(ans, x_len + j_len)
					x_len = max(x_len, j_len)
			return x_len + 1

		dfs(1, -1)
		if  ans >= 2:
			print("NO")
		else:
			print("YES")

if __name__ == '__main__':
    solve()
