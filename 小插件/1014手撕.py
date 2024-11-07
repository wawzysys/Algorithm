class Solution:
    def Lcs(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        max_len = 0
        end_pos = 0
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_pos = i
        return str1[end_pos - max_len:end_pos]

# 示例
solution = Solution()
str1 = "1AB2345CD"
str2 = "12345EF"
result = solution.Lcs(str1, str2)
print(result)  # 输出：'2345'
