import random

def main_solution(n, x, y):
    """主程序：计算相邻点之间的最大斜率"""
    if all(xi == x[0] for xi in x):
        return "undefined"

    # 将点按x坐标排序，同时保持对应的y坐标顺序
    pts = sorted(zip(x, y), key=lambda p: (p[0], p[1]))
    max_slope = float('-inf')

    # 遍历相邻的两个点，计算斜率并更新最大斜率
    for i in range(1, n):
        x1, y1 = pts[i - 1]
        x2, y2 = pts[i]
        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1)
            max_slope = max(max_slope, slope)

    return f"{max_slope:.2f}"

def brute_force_solution(n, x, y):
    """暴力解法：计算所有点对的斜率并找最大值"""
    if all(xi == x[0] for xi in x):
        return "undefined"

    max_slope = float('-inf')

    # 遍历所有点对，计算斜率并更新最大斜率
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] != x[j]:  # 排除x坐标相同的情况
                slope = (y[j] - y[i]) / (x[j] - x[i])
                max_slope = max(max_slope, slope)

    return f"{max_slope:.2f}"

def generate_test_case():
    """随机测试数据生成器"""
    T = 100  # 随机组数
    cases = []
    for _ in range(T):
        n = random.randint(2, 50)  # 控制点数量在合理范围内
        x = [random.randint(0, 100) for _ in range(n)]
        y = [random.randint(0, 100) for _ in range(n)]
        cases.append((n, x, y))
    return cases

def run_test():
    """对拍逻辑：比较主程序和暴力解法的输出"""
    test_cases = generate_test_case()
    all_passed = True

    for case in test_cases:
        n, x, y = case

        # 运行主程序和暴力解法
        main_result = main_solution(n, x, y)
        brute_result = brute_force_solution(n, x, y)

        # 比较输出
        if main_result != brute_result:
            all_passed = False
            print("Test failed!")
            print(f"Input: n = {n}")
            print(f"x = {x}")
            print(f"y = {y}")
            print(f"Main Solution Output: {main_result}")
            print(f"Brute Force Output: {brute_result}")
        else:
            print(f"Test passed for n = {n}")

    if all_passed:
        print("All tests passed!")

if __name__ == "__main__":
    run_test()
