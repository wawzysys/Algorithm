#/E/0Code/Algorithm/meituan/C.py
import sys
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
	n, q = mint()
	mod = int(10 ** 9 + 7)
	powers = [1] * (q + 10)
	for i in range(1, q + 10):
		powers[i] = (powers[i - 1] * 2) % mod

	a = [0] + lint()

	num = [q] * (n + 10)

	for i in range(q):
		c = sint()
		num[c] -= 1
	ans = 0
	for i in range(1, n + 1):
		ans += a[i] * (powers[num[i]]) % (mod)
	print(ans % mod)

if __name__ == '__main__':
	solve()