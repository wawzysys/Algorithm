def f(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for coin in [1, 2, 3]:
        for amout in range(coin, N + 1):
            dp[amout] += dp[amout - coin]
    return dp[N]
N1 = 3
N2 = 2934
print(f(N1))
print(f(N2))
# 思路：动态规划
# 使用一个列表 dp 来存储每个金额对应的兑换方法数。
# dp[i] 表示兑换 i 分的方法数。
# 初始化：dp[0] 被初始化为 1，因为兑换 0 分的方法只有一种，即不使用任何硬币。
# 迭代过程：对于每一种硬币，我们遍历从该硬币面值到 N 的所有金额，
# 并更新 dp[i] 的值。具体来说，
# dp[i] += dp[i - coin] 表示当前金额 i 
# 的方法数增加了使用当前硬币兑换 i - coin 分的方法数。
# 最终结果：dp[N] 即为兑换 N 分的总方法数。
# 时间复杂度：O(N * 3)