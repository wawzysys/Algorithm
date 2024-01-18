
from collections import *
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n, k = mint()
	s = list(input())
	d = defaultdict(int)
	for char in s:
		d[char] += 1
	nums = []
	for c in d:
		nums.append(d[c])
	# print(nums)
	nums.sort()
	nums = nums[::-1]
	# print(nums)
	ans = 0
	num = 0
	for x in nums:
		# print(k,x)
		if k >= x:
			ans += x * x
		else:
			ans += k * k
			break
		k -= x
	print(ans)




if __name__ == '__main__':
    solve()
