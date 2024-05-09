# E:\0Code\Algorithm\acw\97.py 2024-04-02 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
mod = 9901
def qmi(a, k):
    a %= mod
    res = 1
    while k:
        if k & 1:
            res = res * a % mod
        a = a * a % mod
        k >>= 1
    return res
def get_sum(p, k):
    if k == 0:
        return 1
    if k % 2 == 0:
        return (p % mod * get_sum(p, k - 1) + 1) % mod
    if k % 2 == 1:
        return (1 + qmi(p, k // 2 + 1)) *get_sum(p, k  // 2) % mod
a, b = mint()
if a == 0:
    print(0)
elif b == 0:
    print(1)
else:
    res = 1
    i = 2
    while i <= a / i:
        if a % i == 0:
            cnt = 0
            while a % i == 0:
                cnt += 1
                a //= i
            res = res * get_sum(i, cnt * b) % mod
        i += 1
    if a > 1:
        res = res * get_sum(a, b) % mod
    print(res)