import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def solve():
    n, m = mint()
    day = [0] + lint()
    diff = [lint() for _ in range(m)]
    def check(x):
        cha = [0 for _ in range(n + 10)]
        for i in range(x):
            d, ll, rr= diff[i]
            cha[ll] +=d
            cha[rr + 1] -= d
        for i in range(1, n + 1):
            cha[i] += cha[i - 1]
            if cha[i] > day[i]:
                return True
        return False
    l = 0
    r = m
    if not check(m):
        print(0)
    else:
        l = 0
        r = m
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        print(-1)
        print(l)
if __name__ == '__main__':
    t = 0
    if t:
        t = int(input())
        for _ in range(t):
            solve()
    else:
        solve()
