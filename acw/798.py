 # E:\0Code\Algorithm\acw\798.py 2024-03-27 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n,m,q= mint()
a = [[0 for i in range(m + 1)]]
for i in range(n):
    a.append([0] + lint())
b = [[0 for i in range(m + 2)] for j in range(n + 2)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        b[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]
for i in range(q):
    x1, y1, x2, y2, c = mint()
    b[x1][y1] += c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y1] -= c
    b[x2 + 1][y2 + 1] += c
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = b[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        print(a[i][j], end = ' ')
    print()

    