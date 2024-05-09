import sys
sys.setrecursionlimit(1000000)
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
	n, k, M, d = mint()
	# if n == k * M * D:
	# 	return M * D
	ans = -1
	for D in range(1, d + 1):
		xx = n // (k * (D - 1) + 1)
		if xx > M:
			ans = max(D * M, ans)
		else:
			ans = max(D * xx, ans)
	return ans
if __name__ == '__main__':
	# t=int(input())
	# for _ in range(t):
	#     solve()

	ans = solve()
	print(ans)