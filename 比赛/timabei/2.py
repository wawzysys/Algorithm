# C:\Users\19160\Desktop\timabei\2.py 2024-06-22 by 777
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def f(s):
    s = list(s)
    s1 = s[::-1]
    a = 0
    b = 0
    for i in s:
        if i == "1":
            a += 1
        else:
            break
    for i in s1:
        if i == "1":
            b += 1
        else:
            break
    return max(a, b)

def solve():
    m = sint()
    only1 = 0
    max1 = 0
    for i in range(m):
        s = input()
        n = len(s)
        num = f(s)
        if num == n:
            only1 += n
        else:
            max1 = max(max1, num)
    print(max1 + only1)
    
    






if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()