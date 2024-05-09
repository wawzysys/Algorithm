
import sys
sint = lambda: int(input())
mint = lambda: map(int, input().split())
def simulate_square(n, g, x, y):
    rd = {'^': 'v', 'v': '^', '<': '>', '>': '<'}
    mv = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    s = 0
    v = {}  # 用于追踪访问的格子及其方向

    g = [list(row) for row in g]

    while True:
        if x < 0 or x >= n or y < 0 or y >= n:
            return s   
        d = g[x][y]
        p = (x, y)
        if p in v and v[p] == d:
            return -1 
        v[p] = d
        g[x][y] = rd[d]
        dx, dy = mv[d]
        x += dx
        y += dy
        s += 1
n = sint()
g = [list(input()) for _ in range(n)]
x, y = mint()
print(simulate_square(n, g, x - 1, y - 1))
