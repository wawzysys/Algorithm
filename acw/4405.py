#/E/0Code/Algorithm/acw/4405.py
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
#TLE
def solve():#tle
	n, m, k = mint()
	g = [[0 for _ in range(m + 1)] ]
	for _ in range(n):
		g.append([0] + lint())
	# print(g)
	s = [[0 for j in range(m + 1)] for _ in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1,  m + 1):
			s[i][j] = s[i][j - 1] + s[i - 1][j] + g[i][j] - s[i - 1][j - 1]
	def find(x1, y1, x2, y2):
		return s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1]
	ans = 0
	for x1 in range(1, n + 1):
		for y1 in range(1, m + 1):
			for x2 in range(x1 , n + 1):
				for y2 in range(y1, m + 1):
					if find(x1, y1, x2, y2) <= k:
						ans += 1
	print(ans)

if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()