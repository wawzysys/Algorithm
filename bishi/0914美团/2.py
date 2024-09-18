
T = int(input())
for _ in range(T):
    a, b, c, x, y = map(int, input().split())
    left, right = 0, a + b + c
    def check(x):
        l_min = max(0, x - c)
        k_min = max(0, x + y * l_min - b)
        k_max = (a - x) // x
        return k_min <= k_max
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    print(left)


