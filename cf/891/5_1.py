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
    n, k = mint()
    a = ints()
    p = [0] * (n + 1)
    s = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = a[i] + p[i]
        s[i + 1] = a[i] + s[i]
    p.sort()

    def find(x):
        return bisect_left(p, x)
    ans = 0
    tr = FenWick(n + 2)
    for i, x in enumerate(s):
        tr.add(find(x), 1)

    for i, x in enumerate(s):
        tr.add(find(x), -1)
        ans += tr.rangeSum(find(x + k), n)
    print(ans)

if __name__ == '__main__':
    solve()
