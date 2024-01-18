
from collections import *
from heapq import *
from math import  *
import random
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
r = 1

def solve():
	T = sint()
	for _ in range(T):
		n = sint()
		nums = lint()
		s = 0 
		odd = 0 
		f = False
		d = defaultdict(int)
		d[0 - 1 ] += 1
		for i, num in enumerate(nums):
			s += num
			if i & 1 :
				odd += num
			ca = s - 2 * odd
			if ca - 1 in d:
				f = True
				break
			d[ca - 1] += 1
		if f:
			print("YES")
		else:
			print("NO")
if __name__ == '__main__':

    solve()
