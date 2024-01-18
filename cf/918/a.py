
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	T = sint()
	for _ in range(T):
		a = lint()
		a.sort()
		if a[0] == a[1]:
			print(a[2])
		else:
			print(a[0])

if __name__ == '__main__':
    solve()
