# E:\0Code\Algorithm\acw\5154.py 2024-03-29 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7
def qmi(a , k) :
    global mod
    res = 1
    while k :
        if k & 1 :
            res = res * a % mod
        a = a * a % mod
        k >>= 1
    return res
n = sint()
s = input()
mm = -inf
cnt = defaultdict(int)
for c in s:
    cnt[c] += 1
    mm = max(mm, cnt[c])
ans = 0
for k, v in cnt.items():
    if v == mm:
        ans += 1
a = qmi(ans, n)
print(int(a))