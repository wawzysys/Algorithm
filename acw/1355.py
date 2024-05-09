# E:\0Code\Algorithm\acw\1355.py 2024-03-30 by wz
import sys
sys.setrecursionlimit(100000)
from bisect import *
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a = lint()
a.sort()
q = sint()
for _ in range(q):
    k = sint()
    print(bisect_right(a, k))