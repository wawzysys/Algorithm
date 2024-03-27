#/E/0Code/Algorithm/acw/789.py
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
from bisect import bisect_left,bisect,insort
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n, q = mint()
	a = lint()
	for _ in range(q):
		num = sint()
		l = bisect_left(a, num)
		if l == len(a) or a[l] != num:
			print("-1 -1")
		else:
			r = bisect_left(a, num + 1) -1
			print(l, r)


def solve_1():
	m, q = mint()
	a = [-inf] + lint() + [inf]
	n = len(a)
	for _ in range(q):
		num = sint()
		l = 0
		r = n - 1
		#找到 >= num
		# r + 1 true
		# l - 1 fasle
		while l <= r:
			mid = l + r >> 1
			if a[mid] >= num:
				r  = mid - 1
			else:
				l  = mid + 1
		if a[l] == num:
			print(l - 1, end = ' ')
		else:
			print(-1, end = ' ')
		l = 0
		r = n - 1
		while l <= r:
			mid = l + r >> 1
			if a[mid] <= num:
				l = mid + 1
			else:
				r = mid - 1
		if a[r] == num:
			print(r - 1)
		else:
			print(-1)





if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve_1()