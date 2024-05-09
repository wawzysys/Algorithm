#/E/0Code/Algorithm/acw/蓝桥杯/4966.py
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
	s = list(input())
	ans, i = 0, 1

	while  i < len(s):
		l = s[i - 1]
		r = s[i]
		if l == r  or l == '?' or r == '?':
			ans += 1
			i += 2
		else:
			i += 1
	print(ans)
 





if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()