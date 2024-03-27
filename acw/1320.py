#/E/0Code/Algorithm/acw/1320.py
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
	n, k = mint()
	a = [0]
	for _ in range(n):
		a.append(sint())
	s = [0] * (n + 10)
	for i in range(1, n + 1):
		s[i] = s[i - 1] + a[i]
	cnt = defaultdict(int)
	cnt[0] += 1
	ans = 0
	for i in range(1, n + 1):
		kk = s[i] % k
		ans += cnt[kk]
		cnt[kk] += 1
	print(ans)








if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()