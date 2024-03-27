def minSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case
    for i in range(1, n + 1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]

# 计算数字1770和1800所需的最少平方数数量
min_squares_1770 = minSquares(1)
min_squares_1800 = minSquares(9999)

print(min_squares_1770, min_squares_1800)
