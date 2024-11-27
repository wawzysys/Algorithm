def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    a = []
    index = 2
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(int(data[index]))
            index += 1
        a.append(row)
    
    # 计算行前缀和
    row = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            row[i][j] = row[i][j - 1] + a[i - 1][j - 1]
    
    # 计算列前缀和
    col = [[0] * (n + 1) for _ in range(m + 1)]
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            col[j][i] = col[j][i - 1] + a[i - 1][j - 1]
    
    max_sum = -10**18
    k_max = min(n - 1, m - 1)
    for k in range(1, k_max + 1):
        for x1 in range(1, n - k + 1):
            for y1 in range(1, m - k + 1):
                x2 = x1 + k
                y2 = y1 + k
                sum_boundary = row[x1][y2] - row[x1][y1 - 1] + row[x2][y2] - row[x2][y1 - 1] + col[y1][x2 - 1] - col[y1][x1] + col[y2][x2 - 1] - col[y2][x1]
                if sum_boundary > max_sum:
                    max_sum = sum_boundary
    print(max_sum)

if __name__ == "__main__":
    main()