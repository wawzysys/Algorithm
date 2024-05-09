# E:\0Code\Algorithm\acw\1215.py 2024-03-28 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

#树状数组
def lbt(x):
    return x & -x

def get(x, a):
    res = 0
    i=x
    while i>0:
        res += a[i]
        i -= lbt(i)
    return res

def fix(x, a):
    i = x
    while i < len(a):
        a[i] += 1
        i += lbt(i)

N = 10 ** 6
while True:
    n = sint()
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(sint() + 5)
    x_cords = sorted(set([x for x in a]))
    x_map  = {x : i for i, x in enumerate(x_cords)}
    a = [x_map[x] for x in a]
    # print(a)
    tr1 = [0] * (N)
    ans = [0] * (n)

    for i in range(n):
        ans[i] = i - get(a[i], tr1)
        fix(a[i], tr1)

    print(sum(ans))
    