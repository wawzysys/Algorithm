class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]   # dp[i][j]表示text1[0,i]范围和text2[0,j]范围构成的最长公共子序列
        dp[0][0] = 1 if text1[0] == text2[0] else 0    # dp[0][0]即为两个字符串首个字符是否相等
        # 处理边界
        for i in range(1, m):
            # 子串text1[1,i]和text2[0]构成的最长公共子序列，相等构成长度为1的子序列，否则不构成
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i-1][0]
        for j in range(1, n):
            # 子串text1[0]和text2[1,j]构成的最长公共子序列，相等构成长度为1的子序列，否则不构成
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j-1]
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                # 如果text1[i] = text2[j]，说明这两个字符可以作为公共子序列的一部分，剩下就看text1[0,i-1]和text2[0,j-1]的最长子序列
                # 否则，要么从text1[0,i-1]和text2[0,j]的最长子序列转移过来，要么从text1[0,i]和text2[0,j-1]的最长子序列转移过来
                dp[i][j] = (1 + dp[i-1][j-1] if text1[i] == text2[j] else max(dp[i-1][j], dp[i][j-1]))
        return dp[m-1][n-1]    # dp[m-1][n-1]表示整个字符串text1和字符串text2构成的最长公共子序列
