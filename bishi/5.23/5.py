def f(matrix, N, K):
    # 构建前缀和矩阵
    b = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            b[i][j] = (matrix[i-1][j-1] +
                                b[i-1][j] +
                                b[i][j-1] -
                                b[i-1][j-1])

    min_sum = float('inf')
    
    # 遍历所有可能的 KxK 子矩阵
    for i in range(K, N + 1):
        for j in range(K, N + 1):
            current_sum = (b[i][j] -
                           b[i-K][j] -
                           b[i][j-K] +
                           b[i-K][j-K])
            min_sum = min(min_sum, current_sum)
    
    return min_sum

# 输入处理
N = int(input().strip())
matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

K = N  
min_value = float('inf')
for k in range(1, N + 1):
    min_value = min(min_value, f(matrix, N, k))

print(min_value)
