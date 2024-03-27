#/E/0Code/Algorithm/acw/4262.py
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
	a = lint()
	b = lint()
	a = [a[i] - b[i] for i in range(n)]
	zheng = 0
	fu = 0
	if a[0] > 0:
		zheng += a[0]
	else:
		fu -= a[0]
	for i in range(1, n):
		x = a[i] - a[i - 1]
		if x > 0:
			zheng += x
		else:
			fu -= x

	print(max(zheng, fu))






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()