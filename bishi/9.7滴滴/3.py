import sys

def solve():
    n, k = map(int, input().split())
    # s = input().strip()
    cost = []
    for _ in range(k):
        cost.append(list(map(int, input().split())))
    s = input().strip()

    def get(x, y):
        return cost[ord(x) - ord('a')][ord(y) - ord('a')]

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1, 2):
        for i in range(n - length + 1):
            j = i + length - 1
            for m in range(i + 1, j, 2):
                dp[i][j] = max(dp[i][j], dp[i][m] + dp[m + 1][j])
            dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + get(s[i], s[j]))

    print(dp[0][n - 1])

if __name__ == "__main__":
    solve()