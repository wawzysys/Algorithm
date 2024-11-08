sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
m = sint()
n = sint()
a1, a2 = mint()
b1, b2 = mint()
k = sint()
blocked = set()
for _ in range(k):
    x, y = mint()
    blocked.add((x, y))
from collections import deque
if (a1, a2) == (b1, b2):
    print(0)
    exit()
if (a1, a2) in blocked or (b1, b2) in blocked:
    print(-1)
    exit()
visited = [[False]*n for _ in range(m)]
q = deque()
q.append((a1, a2, 0))
visited[a1][a2] = True
while q:
    x, y, d = q.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and (nx, ny) not in blocked:
            if (nx, ny) == (b1, b2):
                print(d+1)
                exit()
            visited[nx][ny] = True
            q.append((nx, ny, d+1))
print(-1)
