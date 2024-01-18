
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
	nums = [0] + lint()
	odd = [0 for _ in range(n + 1)]
	s = [0 for _ in range(n + 1)] 

	for i in range(1, n + 1):
		num =nums[i]
		s[i] = s[i - 1] + num
		odd[i] = odd[i - 1]
		if num % 2 == 1:
			odd[i] += 1
		# print("几个",odd[i],"i",i)
		if i == 1:
			print(s[i],end= ' ')
		elif i == 2:
			print(s[i] // 2 * 2 ,end= ' ')
		else:
			if  odd[i] == 0:
				print(s[i],end= ' ' )
			elif odd[i] == 1:
				print(s[i] - 1 ,end= ' ')
			elif odd[i]  == 2:
				print(s[i],end= ' ')
			elif odd[i] >= 3:
				cc = odd[i] // 3
				if odd[i] % 3 == 1:
					cc += 1
				print(s[i] - cc,end= ' ')
	print()
	# print()






if __name__ == '__main__':
	T = sint()
	for _ in range(T):
		solve()
