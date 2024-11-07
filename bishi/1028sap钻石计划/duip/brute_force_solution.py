# 暴力解法：计算所有点对的斜率，找最大值
sint = lambda: int(input())
lint = lambda: list(map(int, input().split()))

def brute_force_solution():
    n = sint()
    x = lint()
    y = lint()

    if all(x1 == x[0] for x1 in x):
        print("undefined")
        return

    max_slope = float('-inf')

    for i in range(n):
        for j in range(i + 1, n):
            if x[i] != x[j]:  # 排除x相同的情况
                slope = (y[j] - y[i]) / (x[j] - x[i])
                max_slope = max(max_slope, slope)

    print(f"{max_slope:.2f}")
