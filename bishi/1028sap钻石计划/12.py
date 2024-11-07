# 定义输入处理函数
sint = lambda: int(input())
lint = lambda: list(map(int, input().split()))

def solve():
    n = sint()  # 点的数量
    x = lint()  # x坐标列表
    y = lint()  # y坐标列表

    # 如果所有点的x坐标相同，则输出undefined
    if all(x1 == x[0] for x1 in x):
        print("undefined")
        return

    # 将点按x坐标排序，同时保持对应的y坐标顺序
    pts = sorted(zip(x, y), key=lambda p: (p[0], p[1]))

    # 初始化最大斜率为负无穷
    max_slope = float('-inf')

    # 遍历相邻的两个点，计算斜率并更新最大斜率
    for i in range(1, n):
        x1, y1 = pts[i - 1]
        x2, y2 = pts[i]
        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1)
            max_slope = max(max_slope, slope)

    # 输出最大斜率，保留两位小数
    print(f"{max_slope:.2f}")

if __name__ == "__main__":
    T = sint()  # 数据组数
    for _ in range(T):
        solve()
