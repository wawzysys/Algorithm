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
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n, m = mint()
	i = 1
	ans = 0
	while i * i <= n:
		if n % i == 0:
			if i >= m:
				ans = max(ans, n // i)
			if n // i >= m:
				ans = max(ans, i)
		i += 1
	print(ans)


if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	    solve()

#	solve()
