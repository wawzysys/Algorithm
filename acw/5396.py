#/E/0Code/Algorithm/acw/5396.py
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
	g = [[0 for i in range(n + 10)] for j in range(n + 10)]
	for i in range(m):
		x1, y1, x2, y2 = mint()
		g[x1][y1] += 1
		g[x2 + 1][y2 + 1] += 1
		g[x1][y2 + 1] -= 1
		g[x2 + 1][y1] -= 1
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			g[i][j] += g[i - 1][j] + g[i][j - 1] - g[i - 1][j - 1] 
			print(g[i][j] % 2, end = '')
		print()






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()