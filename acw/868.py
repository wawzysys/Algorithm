#/E/0Code/Algorithm/acw/868.py
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
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n = sint()
	prime = []
	st = [False] * (n + 10)
	phi = [0] * (n + 10)
	phi[1] = 1
	for i in range(2, n + 1):
		if not st[i]:
			prime.append(i)
			phi[i] = i - 1
		for p in prime:
			if i * p > n:
				break
			st[i * p] = True
			if i % p == 0:
				phi[i * p] = p * phi[i]
				break
			else:
				phi[i * p] = (p - 1) * phi[i]
	print(sum(phi))






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()