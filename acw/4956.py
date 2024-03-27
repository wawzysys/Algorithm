#/E/0Code/Algorithm/acw/4956.py
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
	def check_max(n):
		for a, b in edge:
			if a // n > b:
				return False
		return True
	def check_min(n):
		for a, b in edge:
			if a // n < b:
				return False
		return True



	n = sint()
	edge = []
	for i in range(n):
		edge.append(lint())


	l = 1  # l - 1 = False
	r = 10 ** 9 #  r + 1 = True
	while l <= r:
		mid = l + r >> 1
		if check_max(mid):
			r = mid - 1
		else:
			l = mid + 1
	print(l, end = ' ')
	l = 1  # l - 1 = False
	r = 10 ** 9 #  r + 1 = True
	while l <= r:
		mid = l + r >> 1
		if check_min(mid):
			l = mid + 1
		else:
			r = mid - 1
	print(r)







if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()