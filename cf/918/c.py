
from collections import *
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
		n = sint()
		a = lint()
		s = sum(a)
		if int(sqrt(s)) * int(sqrt(s)) == s:
			print("YES")
		else:
			print("NO")


if __name__ == '__main__':
    solve()
