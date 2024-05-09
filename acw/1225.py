# E:\0Code\Algorithm\acw\1225.py 2024-04-02 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
x = input()
# print(s)
n = len(x)
k = 0
def dfs(x) :
    res = 0 
    global k
    while k < n:
        if x[k] == '(':
            k += 1
            res += dfs(x)
            k += 1
        elif x[k] == ')':
            return res
        elif x[k] == '|':
            k += 1
            res = max(res, dfs(x))
        elif x[k] ==  'x':
            k += 1
            res += 1
        else:
            k += 1
    return res
ans = dfs(x)
print(ans)