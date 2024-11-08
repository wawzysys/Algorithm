MOD = 908244353

def solve(n, k):
    dp = [0] * (n + 1)
    dp[0] = 1
    for length in range(2, n + 1, 2):
        for i in range(0, length, 2):
            dp[length]  = (dp[length] + k * dp[i] * dp[length - 2 - i]) % MOD
    return dp[n]
n, k = map(int, input().split())
print(solve(n, k))