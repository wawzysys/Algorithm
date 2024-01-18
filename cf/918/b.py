
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
		cnt = defaultdict(int)
		for i in range(3):
			s = list(input())
			for c in s:
				if c != '?':
					cnt[c] += 1
		for x in cnt:
			if cnt[x] == 2:
				print(x)



if __name__ == '__main__':
    solve()
