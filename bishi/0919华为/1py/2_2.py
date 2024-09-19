import sys
from collections import deque
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

class so():
    def main(self):
        n = sint()
        k = sint()
        grid = [lint() for _ in range(n)]
        mm = max(grid[0][0], grid[n-1][n-1])
        inf = float('inf')
        mv = -inf
        for i in range(n):
            for j in range(n):
                mv = max(mv, grid[i][j])
        inf = float('inf')
        mv = -inf
        for i in range(n):
            for j in range(n):
                mv = max(mv, grid[i][j])
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        def check(xx):
            if grid[0][0] > xx or grid[n-1][n-1] > xx:
                return False
            vis = [[False]*n for _ in range(n)]
            queue = deque()
            queue.append((0,0))
            vis[0][0] = True
            se = 0
            while queue and se <= k:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if x == n-1 and y == n-1:
                        if se <= k:
                            return True
                    for i in range(4):
                        nx, ny = x + dir[i][0], y + dir[i][1]
                        if 0 <= nx < n and 0 <= ny < n :
                            if not vis[nx][ny] :
                                if grid[nx][ny] <= xx:
                                    vis[nx][ny] = True
                                    queue.append((nx, ny))
                se +=1
            return False
        l = mm
        r = mv
        while l < r:
            mid = (l + r) //2
            if check(mid):
                r = mid
            else:
                l = mid +1
        print(l)

a = so()
a.main()