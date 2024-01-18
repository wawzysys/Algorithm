
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
		a, b, c = input().split()
		a = int(a);c=int(c)
		if b == 'KB':
			a *= 1024
		if b == 'MB':
			a *= 1024 * 1024
		print(a  // c)


if __name__ == '__main__':
    solve()
