#/E/0Code/Algorithm/acw/3224.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solve():
	m, n, q = mint()
	# print(n, m, q)
	g = [['.' for _ in range(n)] for _ in range(m)]
	# -1 表示横着
	# -2 竖着
	# -3 交叉
	# 0 空白
	for _ in range(q):
		op = list(input().split())
		if len(op) == 4:
			x, y, c = int(op[1]), int(op[2]), op[3]
			# vis = set()
			# def dfs(i, j):
			# 	vis.add((i, j))
			# 	g[i][j] =  c
			# 	for k in range(4):
			# 		x = i + dx[k]
			# 		y = j + dy[k]
			# 		if 0 <= x < m and 0 <= y < n and  (x, y) not in vis:
			# 			if g[x][y] == '|' or g[x][y] == '+' or g[x][y] == '-':
			# 				continue 
			# 			dfs(x, y)
			# dfs(x, y)

		elif len(op) == 5:
			x1, y1, x2, y2 = int(op[1]), int(op[2]), int(op[3]), int(op[4])
			y1, y2 = min(y1, y2), max(y1, y2)
			x1, x2 = min(x1, x2), max(x1, x2)

			if x1 == x2: # 横着
				for j in range(y1, y2 + 1):
					if g[x1][j] == '-' or g[x1][j] == '+':
						g[x1][j] = '+'
					else:
						g[x1][j] = '|'
			else:#竖着
				for i in range(x1, x2 + 1):
					if g[i][y2] == '|' or g[i][y2] == '+':
						g[i][y2] = '+'
					else:
						g[i][y2] = '-'
 
	for j in range(n - 1, -1, -1):
		for i in range(m):
			print(g[i][j], end = '')
		print()

if __name__ == '__main__':
	solve()