#/E/0Code/Algorithm/acw/211.py
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
MOD = 10**4 + 7
N = 1010
c = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
	for j in range(i + 1):
		if j == 0: c[i][j] = 1
		else: c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD 
def solve():
	a, b, k, n, m = mint()
	ans = 0

	print(pow(a, n, MOD)* pow(b, m, MOD) * c[k][n] % MOD)




if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()