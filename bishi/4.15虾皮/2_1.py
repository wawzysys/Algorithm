# def largestNumber(costs, coins) -> list:
#     costs_copy = costs.copy()
#     a = []
#     for i, x in enumerate(costs):
#         a.append([x, i])
#     a.sort()
#     ans = []
#     for x, i in a:
#         if coins - x >= 0:
#             ans.append(i)
#             coins -= x
#         else:
#             break
#     ans.sort()
#     anss = []
#     for i in ans:
#         anss.append(costs_copy[i])
#     return anss
# a = list(map(int, input().split()))
# b = int(input())
# print(*largestNumber(a, b))
#/E/0Code/Algorithm/bishi/虾皮/2_1.py

from heapq import heapify,heappush,heappop

# def largestNumber(costs, coins):
#     w = coins
#     n = len(costs)
#     weights = [0] + costs
#     items = list(enumerate(weights))
#     items.sort(key=lambda x: x[1], reverse=True)  
#     dp = [[0] * (w + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for j in range(w + 1):
#             dp[i][j] = max(dp[i][j], dp[i - 1][j])
#             if j - items[i-1][1] >= 0:
#                 dp[i][j] = max(dp[i][j], dp[i - 1][j - items[i-1][1]] + 1)
    
#     now = dp[n][w]
#     ans = []
#     for i in range(n, 0, -1):
#         if w - items[i-1][1] >= 0 and dp[i - 1][w - items[i-1][1]] + 1 == now:
#             now -= 1
#             w -= items[i-1][1]
#             ans.append(items[i-1][0])
    
#     ans.sort()
#     answer = [weights[i] for i in ans]
#     return answer
def max_number(costs, coins):
    f = [0] * (coins + 1)  # 用于存储最多可以购买的物品数
    rec = [[] for _ in range(coins + 1)]  # 用于存储购买序列

    # 遍历每个成本
    for cost in costs:
        # 从coins到cost反向遍历，确保每个物品只被计算一次
        for j in range(coins, cost - 1, -1):
            # 如果使用当前成本可以购买更多物品
            if f[j - cost] + 1 > f[j]:
                # 更新最多物品数
                f[j] = f[j - cost] + 1
                # 更新购买序列
                rec[j] = rec[j - cost] + [cost]

    # 返回达到总硬币数时的购买序列
    return rec[coins]


a = list(map(int, input().split()))
b = int(input())
print(*largestNumber(a, b))
