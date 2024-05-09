# E:\0Code\Algorithm\acw\1209.py 2024-04-02 by wz
from functools import cache
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
path = [0] * 9
vis = set()
ans = 0
n = int(input())  
def puut(l, r, path):
    d = 0
    for i in range(l, r + 1):  
        d = d * 10 + path[i]
    return d
def dfs(u, path_tuple):  
    global ans

    path = list(path_tuple)  
    if u == 9:
        for i in range(7):
            tep1 = puut(0, i, path)
            if tep1 >= n:
                return 
            for j in range(i + 1, 8):
                tep2 = puut(i + 1, j, path)
                tep3 = puut(j + 1, 8, path)
                if tep1 * tep3 + tep2 == n * tep3:
                    ans += 1
        return

    for i in range(9):
        if i not in vis:
            vis.add(i)
            path[u] = i + 1
            dfs(u + 1, tuple(path))  
            vis.remove(i)

dfs(0, tuple(path))
print(ans)