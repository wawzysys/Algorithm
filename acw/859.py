#/E/0Code/Algorithm/acw/859.py
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
inf = float("inf")
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
def kruskal(n, edges):
    dsu = DSU(n)
    edges.sort(key = lambda x : x[2])
    res = 0
    for u, v, w in edges:
        if dsu.same(u, v):
            continue
        dsu.union(u, v)
        res += w
    return res if dsu.setCount == 1 else "impossible"

def solve():
    n, m = mint()
    g = []
    for _ in range(m):
        x, y, d =  mint()
        g.append([x - 1, y - 1, d])
    print(kruskal(n, g))
	






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()