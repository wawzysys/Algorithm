#/E/0Code/Algorithm/acw/870_1.py
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
	mod = 10**9 +7
	T = sint()
	ans = 1
	num = defaultdict(int)
	for _ in range(T):
		n = sint()
		i = 2
		while i * i <= n:
			if n % i == 0:
				tep = 0
				while n % i == 0:
					tep += 1
					n //= i
				num[i] += tep
			i += 1
		if n > 1:
			num[n] += 1
	for p, k in num.items():
		ans = ans *  (1 - pow(p, k + 1 , mod)) * pow(1 - p, mod - 2, mod)
	print(ans % (10**9 + 7))






if __name__ == '__main__':
	# t=int(input())
	# for _ in range(t):
	#   solve()

	solve()