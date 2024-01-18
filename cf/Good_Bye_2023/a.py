
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	m, k = mint()
	a = lint()
	pp = 1
	for num in a:
		pp *= num
	ans = [1, 7, 17, 17 * 7, 17 * 17, 2023]
	if pp in ans:
		print("YES")
		res = [2023 // pp]
		for i in range(k - 1):
			res.append(1)
		for num in res:
			print(num, end = ' ')
		print()
		return 
	else:
		print("NO")
		return 


if __name__ == '__main__':
	T = sint()
	for _ in range(T):
		solve()
