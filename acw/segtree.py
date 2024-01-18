#lfss
class segtree:
    __slots__ = 'left', 'right', 'l', 'r', 'val'
    def __init__(self,l,r):
        self.left = self.right = None
        self.l,self.r,self.val = l,r,-1
    def build(self):
        mid = self.l+self.r>>1
        if not self.left:self.left = segtree(self.l,mid)
        if not self.right:self.right = segtree(mid+1,self.r)
    def up(self,idx,val):
        if self.l == self.r:
            self.val = max(self.val,val)
            return
        mid = self.l+self.r>>1
        self.build()
        if idx <= mid:self.left.up(idx,val)
        else:self.right.up(idx,val)
        self.val = max(self.left.val,self.right.val)
    def find(self,low,hig):
        if low == self.l and hig == self.r:return self.val
        mid = self.l+self.r>>1
        self.build()
        res = -1
        if low <= mid:res = max(self.left.find(low,min(hig,mid)),res)
        if hig >= mid+1:res = max(res,self.right.find(max(low,mid+1),hig))
        return res
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        m = len(queries)
        mx = 10**9+10
        b = []
        ans = [-1]*m
        for i in range(m):
            b.append([queries[i][0],queries[i][1],i])
        b.sort()
        a = [[i,j] for i,j in zip(nums1,nums2)]
        a.sort()
        seg = segtree(0,mx)
        while b:
            x,y,z = b.pop()
            while a and a[-1][0] >= x:
                seg.up(a[-1][1],a[-1][1]+a[-1][0])
                a.pop()
            ans[z] = seg.find(y,mx)
        return ans


####
#import sys
from collections import defaultdict
# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
class BookMyShow:

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
    
    '''自定义bisect函数：二分查找'''
    # 在区间[left, rgiht]中二分查找到第一个剩余座位数>=x的排号【bisect_left】
    def bisect(self, x, left, right, root):
        if left == right:
            return left
        mid = (left + right) // 2
        if self.max[2*root] < x:        # 左子树不行，往右子树找
            return self.bisect(x, mid+1, right, 2*root+1)
        else:           # 左子树若行，收缩区间，往左子树继续寻找【bisect_left】
            return self.bisect(x, left, mid, 2*root)
    
#lazy

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.max = [0] * (4*n)      # 维护区间最大值
        self.sum = [0] * (4*n)      # 维护区间和
        self.lazy = [-1] * (4*n)    # 懒更新标记【初始化为-1，有助于判断】
        self.build(m, 1, n, 1)      # 建树【线段树下标从1开始】
    
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
    
    '''自定义pushDown函数：下推懒更新标记'''
    # 延迟更新值为0，因此无需记录左右子树大小
    def pushDown(self, root):
        if self.lazy[root] >= 0:
            self.max[2*root] = self.sum[2*root] = self.lazy[root]
            self.max[2*root+1] = self.sum[2*root+1] = self.lazy[root]
            self.lazy[2*root] = self.lazy[2*root+1] = self.lazy[root]
            self.lazy[root] = -1

    '''自定义add函数：单点更新'''
    # 在区间[left, right]中将区间[i]的值+val
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
    
    '''自定义update函数：区间更新'''
    # 在区间[left, right]中更新区间[L,R]的值为val
    def update(self, L, R, val, left, right, root):
        if L<=left and right<=R:
            self.max[root] = val    # root节点更新为val
            self.sum[root] = val    # root节点更新为val
            self.lazy[root] = val   # 懒更新
            return
        mid = (left+right) // 2
        self.pushDown(root) # 【勿忘我】
        if L <= mid:        # 左区间有重合
            self.update(L, R, val, left, mid, 2*root)
        if R > mid:         # 右区间有重合
            self.update(L, R, val, mid+1, right, 2*root+1)
        self.pushUp(root)

    '''自定义query函数：区间和查询'''
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
    
    '''自定义bisectMax函数：二分查找区间最大值'''
    # 在区间[left, rgiht]中二分查找到第一个剩余座位数>=x的排号i，刚好满足max[1,i]>=x【bisect_left】
    def bisectMax(self, x, left, right, root):
        if left == right:
            return left
        mid = (left + right) // 2
        if self.max[2*root] < x:        # 左子树不行，往右子树继续寻找
            return self.bisectMax(x, mid+1, right, 2*root+1)
        else:           # 左子树若行，往左子树继续寻找【收缩区间，bisect_left】
            return self.bisectMax(x, left, mid, 2*root)
    
    '''自定义bisectSum函数：二分查找区间和'''
    # 在区间[left, rgiht]中二分查找到剩余座位总数>=x的排号i，刚好满足sum[1,i]>=x【bisect_left】
    #【bisectSum二分时，当左子树区间和<x时，应将x减去左子树的区间和，再继续去右子树二分寻找】
    def bisectSum(self, x, left, right, root):
        if left == right:
            return left
        mid = (left + right) // 2
        if self.sum[2*root] < x:    # 左子树不行，往右子树找【应先减去左子树，再去右子树继续寻找剩余部分】
            return self.bisectSum(x-self.sum[2*root], mid+1, right, 2*root+1)
        else:           # 左子树若行，往左子树继续寻找【收缩区间，bisect_left】
            return self.bisectSum(x, left, mid, 2*root)


    def gather(self, k: int, maxRow: int) -> List[int]:
        if k > self.m or self.max[1] < k:
            return []
        i = self.bisectMax(k, 1, self.n, 1)     # 区间[1,n]中寻找第一个空位数>=k的排i
        if i > maxRow + 1:                      # i排超出maxRow+1，无解
            return []
        rest = self.query(i, i, 1, self.n, 1)   # 第i排剩余的空位数
        self.add(i, -k, 1, self.n, 1)           # 更新：第i排填充k人
        return [i-1, self.m-rest]


    def scatter(self, k: int, maxRow: int) -> bool:
        if self.sum[1] < k:
            return False
        rest = self.query(1, maxRow+1, 1, self.n, 1)    # [1,maxRow+1]排剩余的空位总数
        if rest < k:
            return False
        start = self.bisectMax(1, 1, self.n, 1)     # 找到第一个有空位置（即最大值为1）的排i
        i = self.bisectSum(k, 1, self.n, 1)         # 找到第i排，使得前i排总空位数刚好>=k
        rest = self.query(start, i, 1, self.n, 1)   # 前i行还剩多少空位置
        if i > start:                               # 前i-1行被填满
            self.update(start, i-1, 0, 1, self.n, 1)
        self.update(i, i, rest-k, 1, self.n, 1)     # 第i行更新为rest-k
        return True


#0x3f
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (n * 4)
        self.sum = [0] * (n * 4)

    # 将 idx 上的元素值增加 val
    def add(self, o: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m: self.add(o * 2, l, m, idx, val)
        else: self.add(o * 2 + 1, m + 1, r, idx, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self.query_sum(o * 2, l, m, L, R)
        if R > m: sum += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum

    # 返回区间 [1,R] 中 <= val 的最靠左的位置，不存在时返回 0
    def index(self, o: int, l: int, r: int, R: int, val: int) -> int:
        if self.min[o] > val: return 0  # 说明整个区间的元素值都大于 val
        if l == r: return l
        m = (l + r) // 2
        if self.min[o * 2] <= val: return self.index(o * 2, l, m, R, val)  # 看看左半部分
        if m < R: return self.index(o * 2 + 1, m + 1, r, R, val)  # 看看右半部分
        return 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
        if i == 0: return []
        seats = self.query_sum(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)  # 占据 k 个座位
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1) < k:
            return False  # 剩余座位不足 k 个
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  # 从第一个没有坐满的排开始占座
        while True:
            left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
            if k <= left_seats:  # 剩余人数不够坐后面的排
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1
