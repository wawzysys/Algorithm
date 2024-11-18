def generate_permutations(n):
    nums = list(range(1, n + 1))
    results = []
    used = [False] * n
    path = []
    def backtrack():
        if len(path) == n:
            results.append(''.join(map(str, path)))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
    backtrack()
    for perm in results:
        print(perm)
n = int(input())
generate_permutations(n)


# 时间复杂度是  O(n!)
# 初始化：
# 创建一个列表 nums，包含从 1 到 n 的数字。
# 创建一个空列表 permutations，用于存储所有排列。
# 回溯函数 backtrack：
# backtrack 函数是一个递归函数，用于生成排列。
# first 参数表示当前正在处理的数字的索引。
# 如果 first 等于 n，说明已经生成了一个完整的排列，将其添加到 permutations 列表中。
# 否则，遍历从 first 到 n-1 的所有索引 i，交换 nums[first] 和 nums[i]，
# 然后递归调用 backtrack(first + 1)，最后恢复交换（回溯）。
# 生成排列：
# 调用 backtrack(0) 开始生成排列。
# 输出结果：
# 遍历 permutations 列表，逐行输出每个排列。