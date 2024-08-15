t = int(input())
for _ in range(t):
    n = int(input())
    jobs = [list(map(int, input().split())) for _ in range(n)]
    jobs.sort(key = lambda x : x[1])
    dp = [0 for _ in range(5001)]
    for i in range(n):
        a = jobs[i][2]
        b = jobs[i][0]
        c = jobs[i][1]
        for j in range(c - b, -1, -1):
            if dp[j] + a > dp[j + b]:
                dp[j + b] = dp[j] + a
    print(max(dp))