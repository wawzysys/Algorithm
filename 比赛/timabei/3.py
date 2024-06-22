
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
mod = 998244353
#组合数

class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def comb(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n - 1] * self.g[n] % self.mod
def solve():
    x1, y1, x2, y2 , n, p, q = mint() 
    a = x2 - x1
    b = y2 - y1
    if a < 0 or b < 0 or a + b != n:
        print(0)
        return 
    ans = f.comb(n, a) * pow(p, a, mod) * pow(q, b, mod) % mod * pow(100, -(a + b), mod) % mod
    print(ans)
if __name__ == '__main__':
    f = Factorial(4 * (10 ** 3) + 10, mod)
    t=int(input())
    for _ in range(t):
      solve()
    # solve()
