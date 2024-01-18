
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n, a = mint()
	nums = [inf] + lint()
	ans = 0
	for i in range(1, n + 1):
		if nums[i - 1] < a and nums[i] >= a:
			ans += 1
	print(ans)
if __name__ == '__main__':
    solve()
