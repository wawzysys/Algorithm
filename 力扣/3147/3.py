from functools import cache


inf = float('inf')
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        @cache
        def dfs(i, j):
            res = -inf
            for x, y in (i + 1, j), (i, j + 1):
                if 0 <= x < n and 0 <= y < m:
                    res = max(res, max(dfs(x, y), 0) + grid[x][y] - grid[i][j])
            return res
        ans = -inf
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans
sc = Solution()
print(sc.maxScore(grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]))