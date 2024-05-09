#/E/0Code/Algorithm/acw/蓝桥杯/197.py
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
g = defaultdict(int)
def is_prime(n: int) -> dict:
	st = [False] * (n + 10)
	prime = defaultdict(int)
	for i in range(2, n + 1):
		if not st[i]:
			prime[i] = 1
		for j in prime:
			if j * i > n:
				break
			st[j * i] = True
			if i % j == 0:
				break
	return prime
def solve():
	n = sint()
	prime = is_prime(n)
	for i in range(2, n + 1):
		if not i in prime: continue
		x , ans = i, 0
		while x <= n:
			ans += n // x
			x *= i
		print(i, ans)


if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()