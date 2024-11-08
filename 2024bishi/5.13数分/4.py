def month_diff(date1, date2):
    # 解析年份和月份
    year1, month1 = int(date1[:4]), int(date1[4:])
    year2, month2 = int(date2[:4]), int(date2[4:])
    
    # 计算月份差
    diff = (year1 - year2) * 12 + (month1 - month2)
    
    # 返回绝对值，因为月份差不应该是负数
    return abs(diff)

# 测试
print(month_diff('202001', '201804'))  # 输出 21
print(month_diff('202001', '202003'))  # 输出 2
