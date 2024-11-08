import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx]); idx +=1
    K = int(data[idx]); idx +=1
    grid = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(data[idx]))
            idx +=1
        grid.append(row)
    min_required = max(grid[0][0], grid[N-1][N-1])
    max_value = max(max(row) for row in grid)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    def can_reach(P):
        if grid[0][0] > P or grid[N-1][N-1] > P:
            return False
        visited = [[False]*N for _ in range(N)]
        queue = deque()
        queue.append((0,0))
        visited[0][0] = True
        steps = 0
        while queue and steps <= K:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if x == N-1 and y == N-1:
                    if steps <= K:
                        return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] <= P:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            steps +=1
        return False
    left = min_required
    right = max_value
    while left < right:
        mid = (left + right) //2
        if can_reach(mid):
            right = mid
        else:
            left = mid +1
    print(left)

main()
