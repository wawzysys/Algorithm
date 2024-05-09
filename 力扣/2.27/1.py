class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        def change(i, j):
            if grid[i][j] == "B":
                grid[i][j] = "W"
            else:
                grid[i][j] = "B"
        def check(i, j):
            if i + 1 < n and j + 1 < m:
                if grid[i][j] == grid[i + 1][j] == grid[i][j + 1] == grid[i + 1][j + 1]:
                    return True
            if i - 1 >= 0 and j - 1 >= 0:
                if grid[i][j] == grid[i - 1][j] == grid[i][j - 1] == grid[i - 1][j - 1]:
                    return True
            if i + 1 < n and j - 1 >= 0:
                if grid[i][j] == grid[i + 1][j] == grid[i][j - 1] == grid[i + 1][j - 1]:
                    return True
            if i - 1 >= 0 and j + 1 < m:
                if grid[i][j] == grid[i - 1][j] == grid[i][j + 1] == grid[i - 1][j + 1]:
                    return True
            return False
        for i in range(n):
            for j in range(m):
                if check(i, j):
                    return True
                change(i, j)
                if check(i, j):
                    return True
                change(i, j)
        return False
                