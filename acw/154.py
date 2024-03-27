#/E/0Code/Algorithm/acw/154.py
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
	n, k = mint()
	a = lint()
	q = deque()
	ans_max = []
	ans_min = []
	#
	for i in range(n):
		while q and a[i] > a[q[-1]]:
			q.pop()
		q.append(i)
		if q[0] == i - k:
			q.popleft()
		if i >= k - 1:
			ans_max.append(a[q[0]])
	q.clear()
	for i in range(n):
		while q and a[i] < a[q[-1]]:
			q.pop()
		q.append(i)
		if q[0] == i - k:
			q.popleft()
		if i >= k - 1:
			ans_min.append(a[q[0]])
	for c in ans_min:
		print(c, end = ' ')
	print()
	for c in ans_max:
		print(c, end = ' ')


if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()