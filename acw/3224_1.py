#/E/0Code/Algorithm/acw/3224.py
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
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def solve():
	n, m, q = mint()
	g = [[0 for _ in range(m)] for _ in range(n)]
	# -1 表示横着
	# -2 竖着
	# -3 交叉
	# 0 空白
	for _ in range(q):
		op = list(input().split())

		if len(op) == 4:
			x, y, c = int(op[1]), int(op[2]), op[3]
			stack = [(x, y)]  # 初始化栈，起始点为(i, j)
			vis = set()  # 访问过的点集合
			while stack:
				i, j = stack.pop()  # 弹出栈顶元素
				if (i, j) in vis:  # 如果该点已访问，跳过
					continue
				vis.add((i, j))  # 标记为已访问
				g[i][j] = ord(c)
				for k in range(4):
					x = i + dx[k]
					y = j + dy[k]
				# 检查新点是否有效
					if 0 <= x < n and 0 <= y < m and g[x][y] >= 0 and (x, y) not in vis:
						stack.append((x, y))  # 加入栈中以后续访问
		elif len(op) == 5:
			x1, y1, x2, y2 = int(op[1]), int(op[2]), int(op[3]), int(op[4])
			y1, y2 = min(y1, y2), max(y1, y2)
			x1, x2 = min(x1, x2), max(x1, x2)

			if x1 == x2: # 横着
				for j in range(y1, y2 + 1):
					if g[x1][j] == -2 or g[x1][j] == -3:
						g[x1][j] = -3
					else:
						g[x1][j] = -1
			else:#竖着
				for i in range(x1, x2 + 1):
					if g[i][y2] == -1 or g[i][y2] == -3:
						g[i][y2] = -3
					else:
						g[i][y2] = -2
 
	for j in range(m-1, -1, -1):
		for i in range(n):
			if g[i][j] == 0:
				print(".", end = '')
			if g[i][j] == -2:
				print("-", end = '')
			if g[i][j] == -1:
				print("|", end = '')
			if g[i][j] ==  -3:
				print("+", end = '')
			if g[i][j] > 0:
				print(chr(g[i][j]), end = '')
		print()

if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()

pri = []
not_prime = [False] * N

def pre(n):
	for i in range(2, n + 1):
		if not not_prime[i]:
			pri.append(i)
		for pri_j in pri:
			if i * pri_j > n:
				break
			not_prime[i * pri_j] = True
			if i % pri_j == 0:
				break
def is_prime(n):
	if n < 2:
		return False
	i = 2
	while i <=n // i:
		if n % i == 0:
			return False
		i += 1
	return True