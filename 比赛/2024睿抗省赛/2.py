import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    def f(n):
        if n == 1: return 12
        if n == 2: return 9
        if n == 3: return 7
        if n == 4: return 5
        if n == 5: return 4
        if n >= 6 and n <= 7: return 3
        if n >= 8 and n <= 10: return 2
        if n >= 11 and n <= 15: return 1
        return 0
    ans = [0 for _ in range(20)]
    t = sint()
    for _ in range(t):
        for i in range(20):
            a, b = mint()
            ans[i] += f(a) + b
    for i in range(20):
        print(i + 1, ans[i])
    
if __name__ == '__main__':
    solve()