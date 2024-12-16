def calculate_optimal_expected_value():
    n = 6 
    expected_rethrow = (n + 1) / 2  
    max_expected = 0
    best_threshold = 1

    for k in range(1, n + 2):  # 阈值k从1到7（包含7）
        if k > n:
            expected = expected_rethrow
        else:
            # 保留的概率
            p_keep = (n - k + 1) / n
            # 保留时的期望值
            expected_keep = sum(range(k, n + 1)) / (n - k + 1)
            # 重新投掷的概率
            p_rethrow = 1 - p_keep
            # 综合期望值
            expected = p_keep * expected_keep + p_rethrow * expected_rethrow

        # 更新最大期望值和最佳阈值
        if expected > max_expected:
            max_expected = expected
            best_threshold = k

    return max_expected, best_threshold

if __name__ == "__main__":
    expected_value, threshold = calculate_optimal_expected_value()
    print(f"最佳策略下的期望值: {expected_value}")
    print(f"最佳保留阈值k: {threshold}")
