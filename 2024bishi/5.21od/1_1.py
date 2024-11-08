m, n = map(int, input().split())

ans = 0
def solve(l, low, high, remain):

    global ans
    if l == m - 1:
        if remain - low <= 3:
            ans += 1
        if ans > 0:
            ans = ans * 2 // 2
        return
    for i in range(low, high + 1):
        remain -= i
        if remain // (m - l - 1) < i:
            break
        solve(l + 1, i, min(i + 3, remain // (m - l - 1)), remain)
        remain += i

if m == 1:
    print(1)
else:
    solve(0, 1, n // m, n)
    print(ans)

