#/E/0Code/Algorithm/acw/蓝桥杯/1221.py
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
	i = 0
	p = []
	c = 0
	g = defaultdict(list)
	while c * c <= n:
		d = c
		while  d * d + c * c <= n:
			s = d * d + c * c
			if not s in g:
				g[s] = [c, d]
			d += 1
		c += 1
	a = 0
	while a * a <= n:
		b = a
		while a * a + b * b <= n:
			s = n - a * a - b * b
			if s in g:
				print(a, b, g[s][0], g[s][1])
				return 
			b += 1

		a += 1











if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()