def arrange_children():
    # 输入并检查数据有效性
    s = input().split()
    for c in s:
        if not c.isdigit():  # 检查是否为正整数
            print("[]")
            return

    # 转换为整数数组
    heights = [int(c) for c in s]

    # 遍历数组并按"高-矮-高-矮"顺序调整
    for i in range(len(heights) - 1):
        # 如果当前位置是"高"位，但当前数比下一个数小
        # 或者当前位置是"矮"位，但当前数比下一个数大
        if (i % 2 == 0 and heights[i] < heights[i + 1]) or \
           (i % 2 == 1 and heights[i] > heights[i + 1]):
            # 交换两个数的位置
            heights[i], heights[i + 1] = heights[i + 1], heights[i]

    # 打印结果，以空格分隔
    print(" ".join(map(str, heights)))

# 调用函数
arrange_children()
