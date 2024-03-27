
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import inf,sqrt,gcd,lcm,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
primes_dict = defaultdict(int)
primes = []
cnt = 0
n = sint()
N = n + 5
st = [0 for _ in range(N)]
def get_primes(n):
	for i in range(2, n + 1):
		if st[i] == 0:
			primes.append(i)
			primes_dict[i] += 1
		for j in primes:
			if j * i > n:
				break
			st[j * i] = 1
			if i % j == 0:
				break
get_primes(n)
# st = [0 for _ in range(n)]
for p in primes:
	if (n - p)
	
