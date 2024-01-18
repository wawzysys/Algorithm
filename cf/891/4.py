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
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def c(arr, k):
    count = 0
    current_sum = 0
    left = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= k and left <= right:
            count += len(arr) - right 
            current_sum -= arr[left]
            left += 1

    return count


def solve():
    n, k = mint()
    a = lint()
    print(c(a,k))






if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()