# E:\0Code\Algorithm\acw\1360.py 2024-03-30 by wz
from functools import cmp_to_key
import sys

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()
from collections import *
from math import *

sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a = set()


def cmp(x, y):
    return x[0] * y[1] - x[1] * y[0]
    #返回 < 0  排序结果 x y
    #返回 > 0  排序结果 y x


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i <= j:
            a.add((i, j))
b = set()
for (i, j) in a:
    b.add((i // gcd(i, j), j // gcd(i, j)))
a = list(b)

a = sorted(a, key=cmp_to_key(cmp))
print("0/1")
for (i, j) in a:

    print(str(i) + "/" + str(j))
