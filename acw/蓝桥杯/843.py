#/E/0Code/Algorithm/acw/蓝桥杯/843.py
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
	n = sint()
	s = defaultdict(int)
	h = defaultdict(int)
	a = defaultdict(int)
	b = defaultdict(int)
	g = [['.' for i in range(n)] for j in range(n)] 
	def dfs(u, x, y):
		# print(u)
		if u == n:
			for i in range(n):
				print(''.join(g[i]))
			print()
			return 
		if y == n:
			x += 1
			y = 0
		if x == n:
			return
		if not x in h and not y in s and  not  x + y in a and not  x - y + n in b:
			h[x] = s[y] = a[x + y] = b[x - y + n] = 1
			g[x][y] = 'Q'
			dfs(u + 1, x + 1, 0)
			g[x][y] = '.'
			del h[x], s[y], a[x + y], b[x - y + n]
		dfs(u, x, y + 1)


	dfs(0, 0, 0)




if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()