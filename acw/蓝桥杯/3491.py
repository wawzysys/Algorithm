#/E/0Code/Algorithm/acw/蓝桥杯/3491.py
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
from math import gcd
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	g = defaultdict(int)
	n = sint()
	i = 2
	ans = 1
	while i * i <= n:
		while n % i == 0:
			g[i] += 1
			n = n // i
		if g[i] & 1:
			ans *= i
		i += 1
	if n > 1:
		ans *= n
	print(ans)







if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()