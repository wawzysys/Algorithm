#/E/0Code/Algorithm/acw/844.py
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
	g = [lint() for _ in range(n)]
	d = [[-1 for _ in range(m)] for _ in range(n)]
	q = deque()
	q.append((0, 0))
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]
	d[0][0] = 0 
	while q:
		tx, ty = q.popleft()
		# print(tx, ty)
		for i in range(4):
			x = tx + dx[i]
			y = ty + dy[i]
			if 0 <= x < n and 0 <= y < m and d[x][y] == -1 and g[x][y] == 0:
				q.append((x,y))
				d[x][y] = d[tx][ty] + 1
	print(d[n - 1][m - 1])





if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()