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
        self.ll = [0] *(4*n+5)
        self.rr = [0] *(4*n+5)
        self.sum = [0] * (4*n+5)  # 维护增量区间和
        self.lazy = [0] * (4*n+5)
        self.build(1, n, 1)  # 建树【线段树下标从1开始】
    
    
    '''自定义pushUp函数：更新节点信息'''
    def pushUp(self, root):
        self.sum[root] = self.sum[2*root] + self.sum[2*root+1]
    
    def pushDown(self, root):
        l = 2 * root
        r = 2 * root + 1
        if self.lazy[root]:
            self.sum[l] += (self.rr[l] - self.ll[l] + 1) * self.lazy[root]
            self.sum[r] += (self.rr[r] - self.ll[r] + 1) * self.lazy[root]
            self.lazy[l] += self.lazy[root]
            self.lazy[r] += self.lazy[root]
            self.lazy[root] = 0
 
        '''自定义build函数：建树'''
    def build(self, left, right, root):
        self.ll[root] = left
        self.rr[root] = right
        if left == right:       # 到达叶子节点，递归终止
            self.sum[root] = b[left - 1]
            return
        mid = (left + right) // 2
        self.build(left, mid, 2*root)  # 左右递归
        self.build(mid+1, right, 2*root+1)
        self.pushUp(root)   

    def change(self, L: int, R: int, val : int,  left: int, right: int, root: int):
        # L,R表示操作区间; root表示当前节点编号(树中)，[left, right]表示root节点所维护的区间
        if L<=left and right<=R:
            self.sum[root] += (self.rr[root] - self.ll[root] + 1) * val
            self.lazy[root] += val
            return 
        self.pushDown(root)
        mid = (left+right) // 2
        if L <= mid:        # 左区间有重合
            self.change(L, R, val, left, mid, 2*root)
        if R > mid:         # 右区间有重合
            self.change(L, R, val, mid+1, right, 2*root+1)
        self.pushUp(root)

    '''自定义query函数：区间和查询'''
    # 查询[L, R]之间合
    # 在区间[left, right]中查询区间[L,R]中的数值之和【求和】
    def query(self, L: int, R: int, left: int, right: int, root: int):
        # L,R表示操作区间; root表示当前节点编号(树中)，[left, right]表示root节点所维护的区间
        if L<=left and right<=R:
            return self.sum[root]
        mid = (left+right) // 2
        self.pushDown(root) # 【勿忘我】
        range_sum = 0
        if L <= mid:        # 左区间有重合
            range_sum += self.query(L, R, left, mid, 2*root)
        if R > mid:         # 右区间有重合
            range_sum += self.query(L, R, mid+1, right, 2*root+1)
        return range_sum
def solve():
    n, m = mint()
    global b
    b =  ints()
    se = segtree(n)
    for _ in range(m):
        tep = input().split()
        if tep[0] == 'C':
            l, r, d = map(int, tep[1:])
            # print(d)
            se.change(l, r, d, 1, n, 1)
            # for i in range(1, n + 1):
            #     print(se.query(i, i, 1, n ,1), end = ' ')
            # print()
        else:
            l, r = map(int, tep[1:])
            ans = se.query(l, r, 1, n, 1)
            print(ans)

if __name__ == '__main__':

    solve()


