def f(a):
    a.sort(reverse=True, key=lambda x: (x[0], x[1]))
    n = len(a)
    dp = [0] * n
    for i in range(n):
        dp[i] = a[i][2]  
    for i in range(n):
        for j in range(i):

            if a[j][0] > a[i][0] and a[j][1] > a[i][1] and a[j][2] > a[i][2]:
                dp[i] = max(dp[i], dp[j] + a[i][2])
    
    return max(dp)
n = int(input())
boxes = [list(map(int, input().split())) for _ in range(n)]
print(f(boxes))
