# E:\0Code\Algorithm\acw\tx1.py 2024-03-31 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n, m = mint()
#并查集
p = list(range(n + 1))
size = [1] * (n + 1)    
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        p[px] = py
        size[py] = size[px] + size[py]
for _ in range(m):
    x, y = mint()
    union(x, y)
a = set()
for i in range(1, n + 1):
    a.add(find(i))
res = 1
# print(a)
if len(a) != 2:
    print(0)
else:
    for i in a:
        res *= size[i]
    print(res)
    
