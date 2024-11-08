import sys
from collections import deque

sint = lambda: int(sys.stdin.readline())
mint = lambda: map(int, sys.stdin.readline().split())
lint = lambda: list(map(int, sys.stdin.readline().split()))

def main():
    m = sint()
    n = sint()
    a1, a2 = mint()
    b1, b2 = mint()
    k = sint()
    blocked = set()
    for _ in range(k):
        x, y = mint()
        blocked.add((x, y))
    if (a1, a2) == (b1, b2):
        print(0)
        return
    if (a1, a2) in blocked or (b1, b2) in blocked:
        print(-1)
        return
    visited = [[False] * n for _ in range(m)]
    q = deque()
    q.append((a1, a2, 0))
    visited[a1][a2] = True
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y, dist = q.popleft()
        if (x, y) == (b1, b2):
            print(dist)
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and (nx, ny) not in blocked:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    print(-1)


main()
