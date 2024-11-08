sint = lambda: int(input())
lint = lambda: list(map(int, input().split()))

def f():
    # 读取输入数据
    n, d = lint()  # 读取队伍数量和允许的最大实力差距
    nums = lint()  # 读取每个队伍的实力值
    
    if n < 2:  # 如果队伍数量不足，无法匹配
        print("-1")
        return

    nums.sort()  # 对队伍实力值进行排序，方便匹配
    ans = 0  # 记录匹配成功的实力差值总和
    used = [False] * n  # 标记每个队伍是否已被匹配

    # 使用贪心策略匹配队伍
    i, j = 0, 1  # 从最小值开始尝试匹配
    while i < n and j < n:
        if i == j or used[i] or used[j]:  # 跳过已匹配的队伍或同一队伍
            j += 1
            continue

        # 如果两个队伍的实力差在允许范围内，则匹配成功
        if abs(nums[j] - nums[i]) <= d:
            ans += abs(nums[j] - nums[i])  # 累计差值
            used[i] = used[j] = True  # 标记已匹配
            i += 1  # 移动到下一个未匹配的队伍
        j += 1  # 继续尝试下一个队伍

    # 检查是否有成功匹配的队伍
    if not any(used):  # 如果没有匹配成功的队伍
        print("-1")
    else:
        print(ans)  # 输出匹配成功的最小实力差值总和

# 调用函数
f()
