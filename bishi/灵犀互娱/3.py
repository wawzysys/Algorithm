from math import gcd
from functools import lru_cache

def f(nums):
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 1

    for i in range(n):
        current_gcd = 0
        for j in range(i, -1, -1):
            current_gcd = gcd(current_gcd, nums[j])
            if current_gcd > 1:
                if j == 0:
                    dp[i] = min(dp[i], 1)
                else:
                    dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[-1]

nums = list(map(int, input().split()))
result = f(nums)
print(result)
