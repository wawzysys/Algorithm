import sys
from collections import *
from math import *
# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
b =[]
class segtree:
    def __init__(self, n: int):
        self.n = n
        # self.m = m
        self.gcd = [1] * (4*n)  # 维护差分区间最大公约数
        self.build(1, n, 1)  # 建树【线段树下标从1开始】
    
    '''自定义build函数：建树'''
    def build(self, left, right, root):
        if left == right:       # 到达叶子节点，递归终止
            self.gcd[root] = b[left]
            return
        mid = (left + right) // 2
        self.build(left, mid, 2*root)  # 左右递归
        self.build(mid+1, right, 2*root+1)
        self.pushUp(root)                   # 更新信息
    
    '''自定义pushUp函数：更新节点信息'''
    def pushUp(self, root):
        self.gcd[root] = gcd(self.gcd[2*root], self.gcd[2*root+1])
    
    '''自定义add函数：单点更新'''
    def add(self, i: int, val: int, left: int, right: int, root: int) -> None:
        # i表示操作位置编号; root表示当前节点编号(树中)，[left, right]表示root节点所维护的区间
        if left == right:           # 到达叶子节点，递归终止
            self.gcd[root] += val   # root节点更新，+val
            return
        mid = (left + right) // 2
        if i <= mid:                # 根据条件判断去往左/右子树
            self.add(i, val, left, mid, 2*root)
        else:
            self.add(i, val, mid+1, right, 2*root+1)
        self.pushUp(root)           # 子节点更新了，父节点信息也需要更新

    #查询[L, R]之间的最大值
    #qeery_max(L,R,1,N,1)
    def query_max(self, L:int, R: int, left :int, right: int, root : int):
        if L <= left and right <= R:
            return self.gcd[root]
        mid = (left + right) // 2
        mm = 0
        if L <= mid:
            mm = self.query_max(L, R, left, mid, 2 * root)
        if R > mid:
            mm = gcd(mm, self.query_max(L, R, mid + 1, right, 2 * root + 1))
        return mm

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

def solve():
    n, m = mint()
    global b
    a = [0] + ints()
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = a[i] - a[i - 1]
    se = segtree(n)
    tr = FenWick(n + 1)
    for _ in range(m):
        tep = input().split()
        l = int(tep[1])
        r = int(tep[2])
        if tep[0] == 'Q':
            l = int(tep[1])
            now = a[int(tep[1])] + tr.rangeSum(1, l)
            print(gcd(now, se.query_max(l + 1, r, 1, n, 1)))
        else:
            x = int(tep[3])
            se.add(l, x, 1, n, 1)
            tr.add(l, x)
            if r < n:
                se.add(r + 1, -x, 1, n, 1)
                tr.add(r + 1, -x)

if __name__ == '__main__':

    solve()

