import sys

RI = lambda: map(int, sys.stdin.readline().split())
RILST = lambda: list(RI())
def solve():
    m, n = RI()
    g = []
    for _ in range(m):
        g.append(RILST())
        g[-1].sort(reverse=True)
        print(g[-1])
    ans = 0
    for i in range(n):
        print(max(g[j][i] for j in range(m)))
        ans += max(g[j][i] for j in range(m))
    print(ans)


if __name__ == '__main__':
    solve()
