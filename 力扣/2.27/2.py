class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        col = [0] * n
        row = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    col[i] += 1
                    row[j] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += (col[i] - 1) * (row[j] - 1)
        return ans