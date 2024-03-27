def can_achieve_sum(prices, excluded, query_sum):
    n = len(prices)
    dp = [[False] * (query_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(query_sum + 1):
            if j >= prices[i - 1] and not excluded[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - prices[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][query_sum]

def main():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    excluded = [False] * n

    for _ in range(m):
        instruction, value = map(int, input().split())
        if instruction == 1:
            print("Yes" if can_achieve_sum(prices, excluded, value) else "No")
        elif instruction == 2:
            # Exclude the piano
            excluded[value - 1] = True

main()
