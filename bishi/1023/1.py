# 定义两个lambda函数用于读取输入数据
sint = lambda: int(input())  # 读取单个整数
lint = lambda: list(map(int, input().split()))  # 读取一行整数并转换为列表

# 输入缓存一个报告所需的金币数 M
M = sint()

# 输入文件标识序列 F 和文件大小序列 S
F = lint()
S = lint()

# 使用字典 d 来存储每个文件的扫描次数和大小
d = {}  
# 遍历文件标识和文件大小，统计每个文件出现的次数和其大小
for f, s in zip(F, S):
    if f in d:
        d[f][0] += 1  # 文件已存在于字典中，增加计数
    else:
        d[f] = [1, s]  # 文件首次出现，初始化计数为1，并存储大小

# 初始化总金币数为0
total = 0

# 遍历字典中的每个文件及其对应的次数和大小
for cnt, size in d.values():
    # 判断是否缓存该文件更合算
    # 如果缓存后续成本(M) 小于 扫描剩余文件的总成本((cnt - 1) * size)
    if M < (cnt - 1) * size:
        total += size + M  # 缓存策略：初次扫描 + 缓存成本
    else:
        total += cnt * size  # 不缓存策略：每次扫描都消耗金币

# 输出最少的金币数
print(total)
