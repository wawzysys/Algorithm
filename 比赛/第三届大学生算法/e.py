
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
from math import gcd
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = sint()
    a = lint()
    g = a[0]
    for i in range(1,n):
        g = gcd(g,a[i])
    if g != 1:
        print (-1)
        return
    ans = n
    for i, v in enumerate(a):
        if v == 1:
            print(1)
            return
        for j in range(i - 1, -1, -1):
            if gcd(a[j], v) == a[j]: break
            a[j] = gcd(a[j], v)
            if a[j] == 1:
                k = i 
                k = i - j
                k += 1
                if k < ans:
                    ans = k
            num = 1
            num += 1
            
    print(ans)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        solve()





