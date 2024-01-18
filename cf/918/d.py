
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n = sint()
	a = input()
	# print(a)
	y = ['a','e']
	ans = []
	if len(a) < 4:
		print(a)
	else:
		i = 0
		while i < n:
			if i >= n - 3:
				tep = a[i:]
				ans.append(tep)
				break
			if  a[i + 3] in y:
				tep = a[i:i + 2]
				i += 2
			else: 
				tep = (a[i:i + 3])
				i += 3
			ans.append(tep)
	l = len(ans)
	for i in range(l):
		if i != l - 1:
			print(ans[i], end = '.')
		else:
			print(ans[i])



if __name__ == '__main__':
	T = sint()
	for _ in range(T):
		solve()
