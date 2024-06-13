---
title: model
abbrlink: d79572d9
date: 2024-05-18 20:23:59
tags:
---
### pymodel
```python
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
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    

if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()
```


### 并查集
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y
```
### 组合数
```python
class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def fac(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def comb(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

    def permu(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[n - m] % self.mod

    def catalan(self, n):
        return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.mod

    def inv(self, n):
        return self.f[n - 1] * self.g[n] % self.mod
```

### 质数筛
```python
pri = []
not_prime = [False] * N

def pre(n):
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
        for pri_j in pri:
            if i * pri_j > n:
                break
            not_prime[i * pri_j] = True
            if i % pri_j == 0:
                break
```
### 质因数个数
```python
def divide(n):
    ans = []
    i = 2
    while i <= n // i:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            ans.append((i, cnt))
        i += 1
    if n > 1:
        ans.append((n, 1))
    return ans
```

### 约数之和
```python
mod = int(1e9 + 7)
primes = {}
a = int(input())
while a:
    a -= 1
    n = int(input())
    i = 2
    while i <= n // i:
        while n % i == 0:
            n //= i
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1
        i += 1
    if n > 1:
        if n in primes:
            primes[n] += 1
        else:
            primes[n] = 1
res = 1
for i,val in primes.items():
    t = 1
    while val:
        val -= 1
        t = (t * i + 1) % mod
    res = res * t % mod
print(res)
```

### 约数个数
```python
mod = 1e9 + 7

primes = {}
a = int(input())
while a:
    a -= 1
    n = int(input())
    i = 2
    while i <= n // i:
        while n % i == 0:
            n //= i
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1
        i += 1
    if n > 1:
        if n in primes:
            primes[n] += 1
        else:
            primes[n] = 1

res = 1
for i in primes.values():
    res = int(res * (i + 1) % mod)
print(res)
```
### 欧拉函数
![alt text](image.png)
```python
n = int(input())
for i in range(n):
    a = int(input())
    res = a
    j = 2
    while j * j <= a :
        if a % j == 0:
            res = res * (j - 1) // j
            while a % j == 0:
                a = a // j
        j += 1
    if a > 1:
        res = res * (a - 1) // a
    print(int(res))
```
### 筛法求欧拉函数
```python
N = 1000010
primes = [0]*N
phi = [0]*N
st = [False]*N

def get_eulers(n):
    phi[1] = 1
    cnt = 0
    for i in range(2,n+1):
        if not st[i]:
            primes[cnt] = i
            cnt += 1
            phi[i] = i - 1
        j = 0
        while primes[j] <= n // i:
            st[primes[j] * i] = True
            if i % primes[j] == 0:
                phi[primes[j] * i] = phi[i] * primes[j]
                break
            phi[primes[j] * i] = phi[i] * (primes[j] - 1)
            j += 1

```

### 扩展欧几里得
![alt text](image-1.png)
```python
def extend_gcd(a,b,x,y):
    if not b:
        return a,1,0

    d,y,x = extend_gcd(b, a % b, y, x)
    y -= a // b * x
    return d,x,y

n = int(input())
while n:
    n -= 1
    a,b = map(int,input().split())
    x,y = 0,0
    d,x,y = extend_gcd(a,b,x,y)
    print(x,y)
```
### 线性同余方程
![20240518200819](https://cdn.jsdelivr.net/gh/wawzysys/imgbed@main/20240518200819.png)
```python
def extend_gcd(a,b,x,y):
    if not b:
        return a,1,0

    d,y,x = extend_gcd(b, a % b, y, x)
    y -= a // b * x
    return d,x,y

n = int(input())
while n:
    n -= 1
    a,b,m = map(int,input().split())
    x,y = 0,0
    d,x,y = extend_gcd(a,m,x,y)
    if b % d:
        print("impossible")
    else:
        print(x * (b // d) % m)
```

### 求组合数
```python
import math
def C(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
n, m = map(int, input().split())
print(C(n, m))
```

## 数据结构

### 树状数组
```python
# 左闭右闭
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
```
### 线段数
```python
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
        # self.build(m, 1, n, 1)  # 建树【线段树下标从1开始】
    
    # '''自定义build函数：建树'''
    # def build(self, val, left, right, root):
    #     if left == right:       # 到达叶子节点，递归终止
    #         self.max[root] = val
    #         self.sum[root] = val
    #         return
    #     mid = (left + right) // 2
    #     self.build(val, left, mid, 2*root)  # 左右递归
    #     self.build(val, mid+1, right, 2*root+1)
    #     self.pushUp(root)                   # 更新信息
    
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
```
### SortedList
```python

class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))
```



### 字符串哈希
```python
class StringHash:
    def __init__(self, s):
        n = len(s)
        self.base = 131
        self.mod = 10 ** 13 + 7
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] * self.base % self.mod
            h[i] = h[i - 1] * self.base + ord(s[i - 1])
            h[i] %= self.mod

        def get_hash(self, l, r):
            res = self.h[r] - self.h[l] * self.p[r - l]
            return res % self.mod
```

### 二维差分
```python
for i in range(1, n + 1):
    for j in range(1, m + 1):
        b[i][j] = a[i][j] - a[i - 1][j] - a[i][j - 1] + a[i - 1][j - 1]
for i in range(q):
    x1, y1, x2, y2, c = mint()
    b[x1][y1] += c
    b[x1][y2 + 1] -= c
    b[x2 + 1][y1] -= c
    b[x2 + 1][y2 + 1] += c
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = b[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]
        print(a[i][j], end = ' ')
    print()
```


## 图论
### spfa
```python
def spfa(u, n, g) -> int:
    q = deque()
    q.append(u)
    vis = set()
    dist = defaultdict(lambda : inf)
    vis.add(u)
    dist[u] = 0
    while q:
        t = q.popleft()
        vis.remove(t)
        for j, d in g[t]:
            if dist[j] > dist[t] + d:
                dist[j] = dist[t] + d
                if j not in vis:
                    vis.add(j)
                    q.append(j)
    return dist[n]
```

### dijkstra
```python
def dij(u, n, g) -> int:
    q = [(0, u)] # 距离 顶点
    vis = set()
    dist = defaultdict(lambda : inf)
    dist[1] = 0
    while q:
        d, u = heappop(q)
        if u in vis:
            continue
        vis.add(u)
        for j, d in g[u]:
            if j not in vis and dist[j] > dist[u] + d:
                dist[j] = dist[u] + d
                heappush(q, (dist[j], j))
    return dist[n]
```

### krushkal
```python
def kruskal():
    dsu = DSU(n)
    edges.sort(key = lambda x : x[2])
    res = 0
    for u, v, w in edges:
        if dsu.same(u, v):
            continue
        dsu.merge(u, v)
        res += w
    return res if dsu.n == 1 else inf
```
