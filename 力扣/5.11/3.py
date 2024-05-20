class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        s = list(s)
        # print(s)
        dp = list(range(n + 1))
        cnt = [[0 for _ in range(n + 1)] for _ in range(26)]
        for i in range(n):
            for j in range(26):
                cnt[j][i + 1] = cnt[j][i]
            cnt[ord(s[i]) - ord('a')][i + 1] += 1
        def check(i, j):
            st = set()
            for k in range(26):
                if cnt[k][j] - cnt[k][i - 1] != 0:
                    st.add(cnt[k][j] - cnt[k][i - 1])
            if len(st) == 1:
                return True
            else:
                return False
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i, 0, -1):
                if check(j, i):
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        # print(dp)
        return dp[n]
        # return 1
s = []
# s.append("ababcc")
s.append("fabccddg")
# s.append("abababaccddb")
for c in s:
    print(Solution().minimumSubstringsInPartition(c))
