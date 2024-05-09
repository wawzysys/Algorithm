#/E/0Code/Algorithm/acw/4646.py
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
# from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	mod = 998244353
	n = sint()
	x = [0]
	y = [0]
	for _ in range(n):
		a, b = mint()
		x.append(a)
		y.append(b)
	f = [0] * (n + 1)
	for i in range(1, n + 1):
		f[i] = (f[i - 1] + 1) * y[i] * pow(y[i] - x[i], mod - 2, mod) % mod
	print(f[n])







if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()