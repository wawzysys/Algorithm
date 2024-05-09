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

#/E/0Code/Algorithm/acw/643.py
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
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def solve():
	r, c = mint()
	g = [list(input()) for _ in range(r)]
	uf = UnionFind(r * c)
	def get_num(x : int, y : int) -> int:
		return x * c + y
	def get_x_y(l):
		return (l // c, l % c)
	zero = 0
	for i in range(r):
		for j in range(c):
			if g[i][j] == '0':
				zero += 1
				continue
			for k in range(4):
				x = i + dx[k]
				y = j + dy[k]
				if 0 <= x < r and 0 <= y < c and g[x][y] == '1':
					uf.union(get_num(i,j), get_num(x, y))
	Q = sint()
	for _ in range(Q):
		op = list(input().split())
		if op[0] == "Q":
			print(uf.part - zero)

		else:
			i, j, z = int(op[1]), int(op[2]), int(op[3])
			if g[i][j] == str(z):
				continue
			if z == 1:# 0 变 1
				zero -= 1
				g[i][j] = '1'
				for k in range(4):
					x = i + dx[k]
					y = j + dy[k]
					if 0 <= x < r and 0 <= y < c and g[x][y] == '1':
						uf.union(get_num(x,y), get_num(i, j))
			else:
				zero += 1
				g[i][j] = '0' # 1 变 0
				for i in range(r):
					for j in range(c):
						uf.root[get_num(i, j)] = get_num(i, j)
				uf.part = r * c
				for i in range(r):
					for j in range(c):
						if g[i][j] == '0':
							continue
						for k in range(4):
							x = i + dx[k]
							y = j + dy[k]
							if 0 <= x < r and 0 <= y < c and g[x][y] == '1':
								uf.union(get_num(i,j), get_num(x, y))				




if __name__ == '__main__':
	t=int(input())
	for _ in range(t):
		print("Case #" + str(_ + 1) + ":")
		solve()

	# solve()