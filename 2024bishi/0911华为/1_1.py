from collections import deque

def min_distance_sum(m, n, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()  
    distances = [[float('inf')] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                queue.append((i, j, 0)) 
                distances[i][j] = 0
    while queue:
        x, y, dist = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                if dist + 1 < distances[nx][ny]:
                    distances[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))
    
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and distances[i][j] != float('inf'):
                res += distances[i][j]
    return res

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

print(min_distance_sum(m, n, grid))  
