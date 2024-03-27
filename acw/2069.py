#/E/0Code/Algorithm/acw/2069.py
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
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1]*n
        self.ans = [0]*n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
            self.ans[x] += self.ans[self.root[x]]
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.ans[root_y] -= self.ans[root_x]
        # 将非根节点的秩赋0
        self.size[root_x] = 0
        self.part -= 1
        return

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # 获取每个根节点对应的组
        part = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        # 获取每个根节点对应的组大小
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size
def solve():
    n, m = mint()
    uf = UnionFind(n + 10)
    ans = [0] * (n + 10)
    for _ in range(m):
        c, a, b = mint()
        if c == 1:
            uf.union(a, b)
        if c == 2:
            tep_size = uf.get_root_part()
            p = uf.find(a)
            for j in tep_size[p]:
                ans[j] += b
    for i in range(1, n + 1):
        print(ans[uf.find(i)] + uf.ans[i], end = ' ')







if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()