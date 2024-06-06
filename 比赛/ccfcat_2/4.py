# coding=utf-8
import sys
from math import isqrt

RI = lambda: map(int, input().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
class PrimeTable:
    def __init__(self, n: int) -> None:
        self.n = n
        self.primes = primes = []  # 所有n以内的质数
        self.min_div = min_div = [0] * (n + 1)  # md[i]代表i的最小(质)因子
        min_div[1] = 1
        # 欧拉筛O(n)，顺便求出min_div
        for i in range(2, n + 1):
            if not min_div[i]:
                primes.append(i)
                min_div[i] = i
            for p in primes:
                if i * p > n: break
                min_div[i * p] = p
                if i % p == 0:
                    break
pt = PrimeTable(10 ** 4 + 5).primes
ping = set()
for i in range(2, 10 ** 6 + 1):
    ping.add(i * i)
def solve():
    n = int(input())
    ans = 1
    for v in pt:
        if v * v > n:
            break
        cnt = 0
        while n % v == 0:
            n //= v
            cnt ^= 1
            if cnt == 0:
                ans *= v
    if n in ping:
        ans *= isqrt(n)
    print(ans)

if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()