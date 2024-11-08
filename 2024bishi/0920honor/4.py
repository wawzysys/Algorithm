split = lambda: input().strip().split()
from collections import Counter
def can_replace(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    shared_letters = sum((c1 & c2).values())
    return shared_letters > (len(s2) / 2)
s1 = split()
s2 = split()
N = len(s1)
M = len(s2)
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = dp[i-1][0] + 1  
for j in range(1, M + 1):
    dp[0][j] = dp[0][j-1] + 2  

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if s1[i-1] == s2[j-1]:

            dp[i][j] = dp[i-1][j-1]
        else:
            if can_replace(s2[j-1], s1[i-1]):
                re = 1
            else:
                re = 3  
            dp[i][j] = min(
                dp[i-1][j] + 1,         
                dp[i][j-1] + 2,         
                dp[i-1][j-1] + re  
            )
tp = dp[N][M]
max_score = N - tp
print(max_score)