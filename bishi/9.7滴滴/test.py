
m, n = map(int, input().split())
a = [float('inf')] * n
s = 0
nums = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    pre = 0
    for j in range(n):
        cur = nums[i][j]
        a[j] = min(a[j], cur - pre)
        pre = cur
        if i == m - 1:
            s += a[j]

print(s)

