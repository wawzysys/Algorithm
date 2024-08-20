def max_players_at_peak(M, server_data):
    # 这个函数接收服务器组数M和对应的每组数据server_data
    # server_data 是一个列表，包含每组服务器的帮会信息列表
    from collections import defaultdict

    results = []
    for data in server_data:
        # 对每组服务器数据进行处理
        events = []
        for entry in data:
            start_time, k, t = entry
            # 转换开始时间为当天开始的分钟数
            start_hour, start_minute = map(int, start_time.split(':'))
            start_minutes = start_hour * 60 + start_minute
            end_minutes = start_minutes + t - 1  # 结束时间是包含的，所以-1分钟

            # 将每个帮会的开始和结束时间添加到事件列表
            events.append((start_minutes, k))  # 开始时刻，人数增加
            events.append((end_minutes + 1, -k))  # 结束后一分钟，人数减少

        # 根据时间排序事件
        events.sort()

        # 扫描所有事件，计算同时在线的最大玩家数
        current_players = 0
        max_players = 0
        for time, change in events:
            current_players += change
            if current_players > max_players:
                max_players = current_players

        results.append(max_players)

    return results


# 示例数据输入
M = 2
server_data = [
    [("09:20", 30, 60), ("10:00", 50, 30), ("11:15", 40, 45)],  # 第一组服务器
    [("09:00", 20, 120), ("09:45", 30, 90), ("10:30", 25, 60)]  # 第二组服务器
]

# 调用函数
output = max_players_at_peak(M, server_data)
for idx, result in enumerate(output):
    print(f"Server Group {idx+1}: Max players at peak is {result}")
