
from collections import deque
from heapq import *
from math import  *
import sys
sys.setrecursionlimit(100000)

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
q = [0] * (int(1e5) + 5)
f = [0] * (int(1e5) + 5)
ll = int(1e5) + 5
pr = [0] * (int(1e5) * 2 + 5)

def is_p(x):
	if x < 2:
		return False
	i = 2
	while i <= x / i:
		if x % i == 0:
			return False
		i+= 1
	return True
def solve():
	n = sint()
	a = [0] + lint()
	for i in range(2, n + 1):
		q[i] = q[ i - 1]
		if pr[a[i] + a[i - 1]] != 1:
			q[i] += 1
	for i in range(n - 1, 0, -1):
		f[i] = f[i + 1]
		if pr[a[i] + a[i + 1]] != 1:
			f[i] += 1
	print(q[:n+ 1])
	print(f[:n+ 1])
	ans = -1
	for i in range(1, n):
		if q[i - 1] or f[i + 2]:
			continue
		if pr[a[i] + a[i + 1]] != 1:
			continue
		if i < n - 1 and pr[a[i] + a[i + 2]] != 1:
			continue
		if i > 1 and pr[a[i + 1] + a[i - 1]] != 1:
			continue
		print(i)
		# if ans != -1:
		# 	print(-1,"wz")
		# 	return 0
		ans = i
		
	print(ans)
if __name__ == '__main__':
	for i in range(2, 200000):
		pr[i] = 1
		temp = int(sqrt(i))
		for j in range(2, temp + 1):
			if i % j == 0:
				pr[i] = 0
				break

	solve()