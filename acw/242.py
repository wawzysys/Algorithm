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
    n, m = mint()
    a = ints()
    tr = FenWick(n + 1)
    for _ in range(m):
        b = list(input().split())
        if b[0] == 'Q':
            x = int(b[1])
            #修改值+原始值
            print(tr.sum(x) + a[x - 1])
        else:
            x = int(b[1])
            y = int(b[2])
            k = int(b[3])
            #差分
            tr.add(x, k)
            tr.add(y + 1, - k)

if __name__ == '__main__':
    solve()
