#/E/0Code/Algorithm/acw/864.py
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
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1]*n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
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
    for _ in range(m):
        x = list(input().split())
        # print(x)
        if x[0] == 'C':
            y = int(x[1])
            z = int(x[2])
            uf.union(y, z)
        if x[0] == 'Q1':
            y = int(x[1])
            z = int(x[2])
            if uf.is_connected(y, z):
                print("Yes")
            else:
                print("No")
        if x[0] == 'Q2':
            y = int(x[1])
            print(uf.size[uf.find(y)])






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()