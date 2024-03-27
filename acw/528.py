#/E/0Code/Algorithm/acw/528.py
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

	n, h, r = mint()
	p = list(range(n))
	def find(x):
		if x != p[x]:
			p[x] = find(p[x])
		return p[x]
	def union(x, y):
		px, py = find(x), find(y)
		if px != py:
			p[px] = py
	def same(x, y):
		return find(x) == find(y)
	low =  []
	high = []
	g = []
	for i in range(n):
		x, y, z = mint()
		if z <= r:
			low.append(i)
		if z + r >= h:
			high.append(i)
		g.append([x, y, z])
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			x1, y1, z1 = g[i]
			x2, y2, z2 = g[j]
			d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
			if d <= (2 * r) ** 2:
				union(i, j)

	for i in low:
		for j in high:
			if same(i, j):
				print("Yes")
				return
	print("No")
	return

if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	  solve()

	# solve()