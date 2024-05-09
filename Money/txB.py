def max_xor_sum(length, segments, nums):
    xor_sum = 0  # 记录最终的和
    current_ones = 0  # 记录当前段内1的个数

    for num in nums:
        if num == 1:
            current_ones += 1
        else:
            xor_sum += current_ones * num  # 当前段内的异或和
            current_ones = 0  # 重置当前段的1的个数

    # 处理最后一个段
    xor_sum += current_ones

    return xor_sum

# 读取输入
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 计算结果并输出
result = max_xor_sum(n, k, nums)
print(result)
