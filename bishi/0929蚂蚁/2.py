sint = lambda: int(input())
mint = lambda: map(int, input().split())
a = lint = lambda: list(map(int, input().split()))

n = sint()
p = a()
dp0, dp1, dp2 = 0, -p[0], -float('inf')
for i in range(1,n):
    x = p[i]
    new0 = max(dp0, dp1 + x)
    new1 = max(dp1, dp0 - x, dp2 + x)
    new2 = max(dp2, dp1 - x)
    dp0, dp1, dp2 = new0, new1, new2
print(dp0)
