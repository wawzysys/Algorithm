import sys
from collections import defaultdict
# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
class segtree:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.max = [0] * (4*n)  # 维护区间最大值
        self.sum = [0] * (4*n)  # 维护区间和
        self.build(m, 1, n, 1)  # 建树【线段树下标从1开始】
    
    '''自定义build函数：建树'''
    def build(self, val, left, right, root):
        if left == right:       # 到达叶子节点，递归终止
            self.max[root] = val
            
            self.sum[root] = val
            return
        mid = (left + right) // 2
        self.build(val, left, mid, 2*root)  # 左右递归
        self.build(val, mid+1, right, 2*root+1)
        self.pushUp(root)                   # 更新信息
    
    '''自定义pushUp函数：更新节点信息'''
    def pushUp(self, root):
        self.max[root] = max(self.max[2*root], self.max[2*root+1])
        self.sum[root] = self.sum[2*root] + self.sum[2*root+1]
    
    '''自定义add函数：单点更新'''
    def add(self, i: int, val: int, left: int, right: int, root: int) -> None:
        # i表示操作位置编号; root表示当前节点编号(树中)，[left, right]表示root节点所维护的区间
        if left == right:           # 到达叶子节点，递归终止
            self.max[root] += val   # root节点更新，+val
            self.sum[root] += val   # root节点更新，+val
            return
        mid = (left + right) // 2
        if i <= mid:                # 根据条件判断去往左/右子树
            self.add(i, val, left, mid, 2*root)
        else:
            self.add(i, val, mid+1, right, 2*root+1)
        self.pushUp(root)           # 子节点更新了，父节点信息也需要更新
    
    '''自定义query函数：区间和查询'''
    # 查询[L, R]之间合
    # 在区间[left, right]中查询区间[L,R]中的数值之和【求和】
    def query(self, L: int, R: int, left: int, right: int, root: int):
        # L,R表示操作区间; root表示当前节点编号(树中)，[left, right]表示root节点所维护的区间
        if L<=left and right<=R:
            return self.sum[root]
        mid = (left+right) // 2
        range_sum = 0
        if L <= mid:        # 左区间有重合
            range_sum += self.query(L, R, left, mid, 2*root)
        if R > mid:         # 右区间有重合
            range_sum += self.query(L, R, mid+1, right, 2*root+1)
        return range_sum

    #查询[L, R]之间的最大值
    #qeery_max(L,R,1,N,1)
    def query_max(self, L:int, R: int, left :int, right: int, root : int):
        if L <= left and right <= R:
            return self.max[root]
        mid = (left + right) // 2
        mm = 0
        if L <= mid:
            mm = self.query_max(L, R, left, mid, 2 * root)
        if R > mid:
            mm = max(mm, self.query_max(L, R, mid + 1, right, 2 * root + 1))
        return mm

def solve():
    m, p = mint()
    se = segtree(m, 0)
    last = 0
    n = 0
    for _ in range(m):
        op, l = input().split()
        l = int(l)
        if op == 'A':
            # print("val", (last + l) % p)
            se.add(n + 1, (last + l) % p, 1, m, 1)
            n += 1
        else:
            last = se.query_max(n - l + 1, n, 1, m, 1 )
            print(last)





if __name__ == '__main__':

    solve()


