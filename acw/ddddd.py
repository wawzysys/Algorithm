
from collections import deque
from heapq import *
from math import  *
import sys
# sys.setrecursionlimit(1000000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def ksm( k,  w, mod):
	cnt = 1
	while w:
		if w % 2:
			cnt *= k
			cnt = cnt % mod
		k = k * k % mod
		w //= 2
	return cnt
def dfs(k, fa, p, a, dp,mod):
	sum = 1
	if k != 1 and len(p[k]) == 1:
		if a[k]:
			dp[k][1] = 1
		else:
			dp[k][0] = 1
		return 
	for i in p[k]:
		if i == fa:
			continue
		dfs(i, k, p,a,dp,mod)
		sum = sum * (dp[i][1] + dp[i][0]) 
		sum = sum % mod

	if a[k] == 1:
	  	dp[k][0] = 0
	  	dp[k][1] = sum
	else:
		dp[k][0] = sum
		for i in p[k]:
			if i == fa:
				continue
			temp = sum * ksm((dp[i][1] + dp[i][0]) , mod - 2, mod) % mod 
			dp[k][1] = dp[k][1] +  temp * dp[i][1]  
			dp[k][1] = dp[k][1] % mod


def solve():
	n = sint()
	a = [0] + lint()
	p = [[] for _ in range(n + 1)]
	summ = 0
	for num in a:
		summ += num
	if summ == 0:
		print(0)
		return
	if n == 1:
		if a[1] == 1:
			print(1)
		else:
			print(0)
		return 0
	dp = [[0, 0] for _ in range(int(1e5) + 5)]
	mod = int(1e9) + 7
	for _ in range(n - 1):
		l, r = mint()
		p[l].append(r)
		p[r].append(l)
	dfs(1,0,p,a,dp,mod)
	print(dp[1][1] % mod)
if __name__ == '__main__':
    solve()
