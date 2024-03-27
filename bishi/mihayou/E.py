import sys
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

sys.setrecursionlimit(3 * 10 ** 5)

from types import GeneratorType


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
    a = [0] + ints()

    bit = FenWick(n + 1)
    f = [0] * (n + 1)

    cnt = 0
    for i in range(n, 0, -1):
        bit.add(a[i], 1)
        cnt += bit.sum(a[i] - 1)
        f[i] = bit.sum(a[i] - 1)

    bit1 = FenWick(n + 1)
    for i in range(1, n + 1):
        bit1.add(a[i], 1)
        f[i] -= bit1.sum(a[i] - 1)

    for i in range(1, n + 1):
        print(cnt - f[i], end=' ')


if __name__ == '__main__':
    solve()
