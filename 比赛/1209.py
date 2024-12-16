def numIslands(grid):
    # 如果网格为空，直接返回岛屿数量为0
    if not grid:
        return 0
    
    # 获取网格的行数和列数
    rows, cols = len(grid), len(grid[0])
    # 初始化岛屿计数器
    count = 0
    
    # 定义深度优先搜索函数
    def dfs(r, c):
        # 如果当前单元格越界或为水（'0'），则返回
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # 将当前单元格标记为已访问（将其值改为'0'）
        grid[r][c] = '0'  
        # 递归探索当前单元格的四个相邻方向（上、下、左、右）
        dfs(r + 1, c)  # 向下
        dfs(r - 1, c)  # 向上
        dfs(r, c + 1)  # 向右
        dfs(r, c - 1)  # 向左
    
    # 遍历整个网格
    for r in range(rows):
        for c in range(cols):
            # 如果当前单元格是陆地（'1'）
            if grid[r][c] == '1':
                # 增加岛屿计数器
                count += 1
                # 调用深度优先搜索函数，探索当前岛屿的所有陆地单元格
                dfs(r, c)
    
    # 返回岛屿的总数量
    return count

# 示例网格
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
# 调用函数计算岛屿数量
ans = numIslands(grid)
# 输出结果
print(ans)  # 输出: 1