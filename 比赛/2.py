n, k = 0, 0
g = []
m = 0

def c(x, y):
    if x + 1 >= n or y + 1 >= n:
        return False
    if g[x][y] or g[x + 1][y] or g[x][y + 1] or g[x + 1][y + 1]:
        return False
    return True

def p(x, y, f):
    g[x][y] = f
    g[x + 1][y] = f
    g[x][y + 1] = f
    g[x + 1][y + 1] = f

def d(x, y, cnt):
    global m
    if y == n:
        x += 1
        y = 0
    if x == n:
        m = max(m, cnt)
        return
    if c(x, y):
        p(x, y, True)
        d(x, y + 2, cnt + 1)
        p(x, y, False)
    d(x, y + 1, cnt)

def main():
    global n, k, g
    n, k = map(int, input().split())
    g = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        g[y][x] = True
    d(0, 0, 0)
    print(m)

if __name__ == "__main__":
    main()
