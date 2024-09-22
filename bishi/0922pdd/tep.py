T = int(input())
for _ in range(T):
    n = int(input())
    P = [0] + [int(input()) for _ in range(n)]  # 1-based indexing

    from collections import defaultdict

    # 初始状态
    dp = defaultdict(lambda: float('inf'))
    dp[(0, 0, 0, 0)] = 0  # (bp, c1, c2, c3): cost

    for day in range(1, n+1):
        dp_new = defaultdict(lambda: float('inf'))
        for (bp, c1, c2, c3), cost in dp.items():
            # 优惠券过期和更新
            new_c1 = c2
            new_c2 = c3
            new_c3 = 0  # 新的优惠券会在下面的操作中更新

            # 选项1：使用优惠券
            if c1 > 0:
                state = (bp, new_c1 - 1, new_c2, new_c3)
                dp_new[state] = min(dp_new[state], cost)
            
            # 选项2：购买汉堡
            price = P[day]
            total_bp = bp + price
            coupons = total_bp // 100
            new_bp = total_bp % 100
            state = (new_bp, new_c1, new_c2, new_c3 + coupons)
            dp_new[state] = min(dp_new[state], cost + price)
        dp = dp_new

    # 找到最小的花费
    result = float('inf')
    for (bp, c1, c2, c3), cost in dp.items():
        result = min(result, cost)

    print(int(result))
