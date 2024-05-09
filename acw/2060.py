# E:\0Code\Algorithm\acw\2060.py 2024-04-02 by wz
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
from math import *
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
n, m = mint()
g = [input() for _ in range(n)]
uf = UnionFind(n * m + 10)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
vis = set()
for i in range(n):
    for j in range(m):
        if g[i][j] != 'X':
            continue
        # print(i * m + j)
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < m and g[i][j] == 'X' and g[x][y] == 'X':
                uf.union(i * m + j, x * m + y)
for i in range(n):
    for j in range(m):
        if g[i][j] == 'X':     
            vis.add(uf.find(i * m + j))
part  = uf.get_root_part()
vis = list(vis)
# print(vis)
def get(num1, num2):
    return abs(num1 // m - num2 // m) + abs(num1 % m - num2 % m)
ans = inf
for num1 in part[vis[0]]:
    for num2 in part[vis[1]]:
        ans = min(ans, get(num1, num2) - 1)
print(ans)