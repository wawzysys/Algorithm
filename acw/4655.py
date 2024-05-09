 # E:\0Code\Algorithm\acw\4655.py 2024-03-27 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
a =[0] +  lint()
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]

b = [0] * (n + 2)
q = sint()
ss_before = 0
for _ in range(q):
    l, r = mint()
    b[l] += 1
    b[r + 1] -= 1 
    ss_before += s[r] - s[l - 1]
for i in range(1, n + 1):
    b[i] += b[i - 1]
a.sort(reverse = True)
b.sort(reverse = True)
ss = 0
for num, cnt in zip(a, b):
    if cnt <= 0:
        break
    ss += num * cnt
print(ss - ss_before)

