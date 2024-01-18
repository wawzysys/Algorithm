import sys
# sys.setrecursionlimit(1000000)
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
	n = sint()
	a = lint()
	cnt = defaultdict(int)
	ans = []
	mm = -inf
	for num in a:
		cnt[num] += 1
		mm = max(mm, num)
	# if len(cnt) == 1:
	# 	for i in range(n):
	# 		print(a[0], end = ' ')
	# 	print()
	# 	return
	###
	c = sorted(cnt)
	j = 0
	ss = cnt[c[j]]
	for i in range(n - 1, 0, -1):
		if ss > i:
			ss -= i
			ans.append(c[j])
		elif ss == i:
			ans.append(c[j])
			if j < len(c) - 1:
				j += 1
				ss = cnt[c[j]]
	# ans.append(c[-1] + 1)
	ans.append(mm + 1)
	#
	for num in ans:
		print(num, end = ' ')
	print()
	return 
if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
	    solve()

	# solve()