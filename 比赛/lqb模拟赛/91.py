n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 计算行和列的前缀和
row_prefix = [[0] * (m + 1) for _ in range(n)]
col_prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        row_prefix[i][j + 1] = row_prefix[i][j] + a[i][j]
        col_prefix[i + 1][j] = col_prefix[i][j] + a[i][j]

max_sum = float('-inf')

for x1 in range(n):
    for y1 in range(m):
        # 最大边长
        max_len = min(n - x1, m - y1)
        for l in range(1, max_len):
            x2 = x1 + l
            y2 = y1 + l

            # 检查是否满足条件
            if x2 >= n or y2 >= m:
                continue

            # 计算左竖和右竖的和
            left_sum = sum(a[x][y1] for x in range(x1, x2 + 1))
            right_sum = sum(a[x][y2] for x in range(x1, x2 + 1))

            # 计算上横和下横的和
            top_sum = sum(a[x1][y] for y in range(y1, y2 + 1))
            bottom_sum = sum(a[x2][y] for y in range(y1, y2 + 1))

            # 总和，减去重复计算的四个角点三次（因为每个角在两条边中被计算了两次）
            total = left_sum + right_sum + top_sum + bottom_sum - 3 * (a[x1][y1] + a[x1][y2] + a[x2][y1] + a[x2][y2])

            if total > max_sum:
                max_sum = total

print(max_sum)