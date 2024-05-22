def countWays(m, n, low, high):
    def helper(m, n, low, high):
        if m == 1:
            return 1 if n - low <= 3  else 0
        ways = 0
        for i in range(low, high + 1):
            n -= i
            if n // (m - 1) < i:
                break
            ways += helper(m - 1, n, i, min(i + 3, n // (m - 1)))
            n += i
        
        return ways
    return helper(m, n, low, high)

# 示例输入输出
m, n = map(int, input().split())
print(countWays(m, n, 1, n // m))
