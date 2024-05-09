#/E/0Code/Algorithm/acw/3999.py
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
from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def oula(n : int) -> int:
	ans = n
	i = 2
	anss = []
	while i * i <= n:
		if n % i == 0:
			anss.append(i)
			while n % i == 0:
				n //= i
		i += 1
	if  n > 1:
		anss.append(n)
	for p in anss:
		ans = ans * (p - 1) / p
	return ans
def solve():
	a, b = mint()
	b = b // gcd(a, b)
	# print("{:.3f} + {}".format(oula(b),oula(b)))
	print(f"{int(oula(b)):d}")






if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	  solve()

	# solve()