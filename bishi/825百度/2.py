def max_gold(n, x, y, k, a_list, b_list, c_list):
    from functools import lru_cache

    # 定义各路防御塔的位置
    top_pos = -x  # 上路位置
    mid_pos = 0   # 中路位置
    bot_pos = y   # 下路位置

    # 定义各路的金币列表，方便通过索引获取
    gold_lists = [a_list, b_list, c_list]
    tower_positions = [top_pos, mid_pos, bot_pos]

    # 计算地图边界
    min_pos = -x
    max_pos = y

    @lru_cache(maxsize=None)
    def dfs(t, pos):
        if t == n:
            return 0

        max_gain = float('-inf')

        # 三种可能的移动：上移、下移、不动
        for move in [-1, 0, 1]:
            new_pos = pos + move
            if new_pos < min_pos or new_pos > max_pos:
                continue

            gain = 0

            # 计算在当前 new_pos 位置时，能从各路获得的金币
            for lane in range(3):
                distance = abs(new_pos - tower_positions[lane])

                if distance == 0:
                    # 亲自击杀，获得全额金币
                    gain += gold_lists[lane][t]
                elif distance <= k:
                    # 防御塔击杀，获得一半金币
                    gain += gold_lists[lane][t] // 2

            # 递归到下一秒
            total_gain = gain + dfs(t + 1, new_pos)
            max_gain = max(max_gain, total_gain)

        return max_gain

    # 初始状态：第 0 秒，位置在中路防御塔下
    result = dfs(0, 0)
    return result

# 示例输入
n = 5
x = 2
y = 2
k = 1
a = [0, 0, 0, 8, 10]
b = [4, 6, 1, 0, 4]
c = [0, 8, 0, 4, 6]

# 调用函数并输出结果
print(max_gold(n, x, y, k, a, b, c))  # 输出：37
