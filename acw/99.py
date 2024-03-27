#/E/0Code/Algorithm/acw/99.py
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
	n, r = mint()
	g = [[0 for i in range(5005)] for j in range(5005)]
	ss = 0
	ans = 0
	for i in range(n):
		x, y, w = mint()
		g[x + 1][y + 1] += w
		ss += w
	if r >= 5001:
		print(ss)
		return
	for i in range(1, 5002):
		for j in range(1, 5002):
			g[i][j] += g[i][j - 1] + g[i - 1][j] - g[i - 1][j - 1]
	for i in range(r, 5002):
		for j in range(r, 5002):
			ans = max(ans, g[i][j] - g[i - r][j] - g[i][j - r] + g[i - r][j - r])
	print(ans)
	






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()