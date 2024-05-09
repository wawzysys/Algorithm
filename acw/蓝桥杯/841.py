#/E/0Code/Algorithm/acw/蓝桥杯/841.py
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

def solve():
	n, m = mint()
	s =  list(' ' + input())
	mod = 10**9 + 7
	P = 1337
	p = [1] * (n + 10)
	h = [0] * (n + 10) 
	for i in range(1, n + 1):
		p[i] = p[i - 1] * P % mod
		h[i] = h[i - 1] * P + ord(s[i])
		h[i] %= mod

	def find(l, r):
		return (h[r] - h[l - 1] * p[r - l +  1]) % mod
	for _ in range(m):
		l1, r1, l2, r2 = mint()
		if find(l1, r1) == find(l2, r2):
			print("Yes")
		else:
			print("No")

if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()