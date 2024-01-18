import functools
import heapq
import itertools
import sys
from typing import Counter

# import itertools
# import math
# import os
# import random

from collections import defaultdict
from functools import lru_cache
from bisect import bisect_left, bisect_right

# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

sys.setrecursionlimit(3 * 10 ** 5)

from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class FenWick:
    def __init__(self, n: int):
        self.n = n
        self.tr = [0 for _ in range(n + 1)]

    def sum(self, i: int):
        i += 1
        s = 0
        while i >= 1:
            s += self.tr[i]
            i &= i - 1
        return s

    def rangeSum(self, l: int, r: int):
        return self.sum(r) - self.sum(l - 1)

    def add(self, i: int, val: int):
        i += 1
        while i <= self.n:
            self.tr[i] += val
            i += i & -i


def solve() -> None:
    n = sint()
    a = ints()
    tr1 = FenWick(n + 2)
    tr2 = FenWick(n + 2)
    g = [0 for _ in range(n)]
    l = [0 for _ in range(n)]
    res1 = 0
    res2 = 0
    for i, num in enumerate(a):
        g[i] = tr1.rangeSum(n + 1, num)
        l[i] = tr1.rangeSum(1,num)
        tr1.add(num, 1)
    for i in range(n - 1, - 1, -1):
        num = a[i]
        res1 += g[i] * (tr2.rangeSum(n + 1, num ))
        res2 += l[i] * (tr2.rangeSum(1, num))
        tr2.add(num, 1)
    print(res1, res2)




if __name__ == '__main__':
    solve()
