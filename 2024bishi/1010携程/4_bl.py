# 直接模拟解法的 Python 实现

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))  # 下标从 1 开始

for _ in range(q):
    op, l, r = map(int, input().split())
    res = a[l]
    idx = l + 1  # 从下一个位置开始

    # 确定操作符的起始顺序
    if op == 1:
        is_and = True  # op = 1，以 & 开始
    else:
        is_and = False  # op = 2，以 | 开始

    # 遍历从 l+1 到 r 的元素，依次应用操作符
    while idx <= r:
        if is_and:
            res = res & a[idx]
        else:
            res = res | a[idx]
        is_and = not is_and  # 切换操作符
        idx += 1

    print(res)
