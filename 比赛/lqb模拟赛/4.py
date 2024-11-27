def min_cost(target):
    dp = [float('inf')] * (target + 1)
    dp[1] = 0
    
    for i in range(1, target + 1):
        if dp[i] == float('inf'):
            continue
        
        # +1 cost 1
        if i + 1 <= target:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        
        # +max digit cost 3
        max_digit = max(int(d) for d in str(i))
        if i + max_digit <= target:
            dp[i + max_digit] = min(dp[i + max_digit], dp[i] + 3)
        
        # *2 cost 10
        if i * 2 <= target:
            dp[i * 2] = min(dp[i * 2], dp[i] + 10)
    
    return dp[target]

print(min_cost(2024))  # 70