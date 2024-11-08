# H 题
import sys

sys.setrecursionlimit(100000)

input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

N = 1000010
pri = []
not_prime = [False] * (N + 1)

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

from bisect import *
pre(N)

def solve() -> None:
    n, q = mint()
    B = 500
    # 下标从0开始
    a = [0] + list(map(int, input().split()))
    st = set(pri)
    b = list(x in st for x in a)
    d = [0] * (n + 1)

    c = [0] * (B + 1)

    for i in range(q):
        op, k, x = map(int, input().split())
        if k >= B:
            for i in range(k, n + 1, k):
                d[i] += -x if op == 2 else x
        else:
            c[k] += -x if op == 2 else x
    
    for x in range(1, B + 1):
        for i in range(x, n + 1, x):
            d[i] += c[x]
    
    ans = []
    for i in range(1, n + 1):
        if d[i]:
            d[i] += bisect_left(pri, a[i])
            if d[i] < 0:
                ans.append(0)
            else:
                if not b[i]:
                    d[i] -= 1
                ans.append(pri[d[i]] if d[i] < len(pri) else 1)
        else:
            ans.append(a[i])    
    # print(*d[:10])            
    print(*ans)

if __name__ == '__main__':
    solve()
