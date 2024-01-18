import sys
from collections import defaultdict
# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
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
    n = sint()
    h = [0]
    #第一个奶牛前面没有比他矮的
    for i in range(n - 1):
        h.append(sint())
    tr = FenWick(n + 2)
    ans = []
    for i in range(1, n + 1):
        tr.add(i, 1)

    #从后往前
    #找到剩下的地h[i]+1矮的奶牛
    for i in range(n - 1, -1, - 1):
        k = h[i] + 1
        l = 1
        r = n + 1
        #r + 1 真
        #l - 1 否
        while l <= r:
            mid = (l + r ) //  2
            if tr.sum(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        #l + 1 = n
        tr.add(l, - 1)
        ans.append(l)
    for num in ans[::-1]:
        print(num)

if __name__ == '__main__':
    solve()
