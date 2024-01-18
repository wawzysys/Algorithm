
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
	if k % m == 0:
		print(k // m * k)
		return
	if gcd(m, k) == 1:
		print(m * k)
		return 
	print(m * k // gcd(m,k))


if __name__ == '__main__':
	T = sint()
	for _ in range(T):
		solve()
