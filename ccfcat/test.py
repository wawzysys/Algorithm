import sys
from functools import *
sys.setrecursionlimit(100000)  # 增加递归深度限制
count = 0
men = [0 for i in range(10 ** 5)]
def dfs(n):
    # print(n)
    global count
    count += 1
    if n == 0:
        return 0
    if men[n] != 0:
        return men[n]
    min_count = float('inf')


    i = 1
    while i**2 <= n:
        min_count = min(min_count, dfs(n - i**2) + 1)
        i += 1
    men[n] += min_count
    return min_count

# 使用记忆化搜索所需的最少平方数
min_squares_dfs = dfs(30)
print(min_squares_dfs) 
print(count)
