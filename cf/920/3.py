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
	n, f, a, b = mint()
	t = [0] + lint()
	l = (b  + a - 1)// a
	# print(l)
	for i in range(1, n + 1):
		if t[i] - t[i - 1] >= l:
			f -= b
		else:
			f -= a * (t[i] - t[i - 1])
		# print(f)
		if f <= 0:
			print("NO")
			return
	print("YES")







if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	    solve()

#	solve()