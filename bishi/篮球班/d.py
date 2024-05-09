# D 题
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def get(x, y):
    ans = 0
    for i, j in zip(x, y):
        if i != j:
            return ans
        ans += 1 
    return ans
def solve():
    f =[[0 for i in range(210)] for j in range(210)]
    n = sint()
    a = [list(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            f[i][j] = get(a[i], a[j])
            ans += f[i][j]
            f[j][i] = f[i][j]
    
    v = 0
    for i in range(n):
        for j in range(len(a)):
            for k in range (ord('a'), ord('z') + 1):
                t = a[i][j]
                a[i][j] = chr(k)
                m = 0
                for z in range (n):
                    if z == i:
                        continue
                    m += get(a[i],a[z])
                    m -= f[i][z]
                v = max(v, ans + m)
                a[i][j] = t
    print(v)


if __name__ == '__main__':
    solve()
