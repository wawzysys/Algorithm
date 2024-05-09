def find_periods(minAvg, rates):
    n = len(rates)
    if n == 0:
        return "NULL"

    # 前缀和数组
    pre_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sums[i] = pre_sums[i - 1] + rates[i - 1]

    max_len = 0
    periods = []

    # 遍历子数组
    for i in range(n):
        for j in range(i, n):
            total = pre_sums[j + 1] - pre_sums[i]
            length = j - i + 1
            avg = total / length

            # 检查条件
            if avg <= minAvg:
                if length > max_len:
                    max_len = length
                    periods = [(i, j)]
                elif length == max_len:
                    periods.append((i, j))

    # 输出
    if max_len == 0:
        return "NULL"
    else:
        return " ".join(f"{s}-{e}" for s, e in sorted(periods))

# 示例输入
m = int(input())
a = list(map(int, input().split()))
print(find_periods(m, a))
