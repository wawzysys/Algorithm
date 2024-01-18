
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
	a = [list(input()) for _ in range(n)]
	b = [list(input()) for _ in range(n)]
	# print(a)
	# print(b)
	for _ in range(4):
		temp = [['0' for _ in range(n)] for _ in range(n)]
		temp1 = [['0' for _ in range(n)] for _ in range(n)]
		temp2 =[['0' for _ in range(n)] for _ in range(n)]
		for i in range(n):
			for j in range(n):
				temp[j][i] = a[i][j]
		for c in temp:
			c.reverse()
		for i in range(n):
			for j in range(n):
				temp1[n - i - 1] = a[i][j]
		for i in range(n):
			for j in range(n):
				temp2[i][n - j - 1] = a[i][j]
		if temp == b or temp1 == b or temp2 == b:
			print("Yes")
			return 
		a = temp
	print("No")




if __name__ == '__main__':
	T = 1
	for _ in range(T):
		solve()
