from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        q = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS
        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        
        return dist
