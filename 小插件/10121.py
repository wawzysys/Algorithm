class Solution:
    def isMatch(self, str: str, pattern: str):
        if not pattern: return not str
        if not str and len(pattern) == 1: return False

        m = len(str) + 1
        n = len(pattern) + 1

        dp = [[False for _ in range(n)] for _ in range(m)]

        dp[0][0] = True
        for j in range(2, n):
            if pattern[j-1] == '*':
                dp[0][j] = dp[0][j - 2]
        for r in range(1, m):
            i = r - 1  # 对应s中的元素
            for c in range(1, n):
                j = c - 1  # 对应p中的元素
                if str[i] == pattern[j] or pattern[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif pattern[j] == '*':
                    if pattern[j - 1] == str[i] or pattern[j - 1] == '.':
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
                else:
                    dp[r][c] = False

        return dp[m - 1][n - 1]
    
a = Solution()
print(a.isMatch("a", "ab*")) 