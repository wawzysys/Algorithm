def calc_charges(logs, prices):
    """
    根据日志和价格计算费用。

    参数:
    - logs (list of str): 日志列表，每条记录格式为 "时间戳,客户ID,计费因子,数量"。
    - prices (list of str): 价格列表，每条记录格式为 "计费因子,单价"。

    返回:
    - list: 按客户ID排序的费用列表，每个元素为元组 (客户ID, 总费用)。
    """

    # 将价格转换为字典，键为计费因子，值为该因子的单价（整数）
    pd = {f: int(p) for f, p in (e.split(',') for e in prices)}
    
    # 初始化客户费用字典和已处理记录集合
    charges = {}
    seen = set()
    
    # 遍历所有日志记录
    for e in logs:
        t, cid, bf, d = e.split(',')  # 分解每条日志记录为时间戳、客户ID、计费因子和数量
        d = int(d)  # 转换数量为整数

        # 检查数量是否在合理范围内，并且这条记录是否已经被处理过
        if not (0 <= d <= 100) or (t, cid, bf) in seen:
            continue  # 如果不符合条件，跳过此条记录
        
        # 将这条记录添加到已处理集合中
        seen.add((t, cid, bf))
        
        # 计算客户费用并累加到客户费用字典中
        charges[cid] = charges.get(cid, 0) + pd.get(bf, 0) * d
    
    # 返回排序后的客户费用列表
    return sorted(charges.items())

# 以下是主程序部分
n = int(input())  # 读取日志数量
logs = [input() for _ in range(n)]  # 读取每条日志
m = int(input())  # 读取价格数量
prices = [input() for _ in range(m)]  # 读取每条价格

# 调用函数并打印结果
for cid, cost in calc_charges(logs, prices):
    print(f'{cid},{cost}')  # 格式化输出每个客户的ID和费用
