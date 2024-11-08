n, k = map(int, input().split())
nums = list(map(int, input().split()))


q = [1] * n  # 初始化所有的 q[i]
p = [1] * n  # 初始化所有的 p[i]

for i in range(n):
    for j in range(n):
        if i != j:
            q[i] *= nums[i] 
            p[i] *= (nums[i] + nums[j])            # 这里应保持原意，只是分母总和
ans_q = 0
ans_p = 1
for c in p:
    ans_p *= c
for i in range(1 << n):
    tep_q = 0
    if bin(i).count('1') == k:
        tep_q = 1
        for j in range(n):
            if i >> j & 1:
                tep_q *= q[j]
            else:
                tep_q *= p[j] - q[j]
    ans_q += tep_q
print(ans_q)
print(ans_p)
print(ans_q/ ans_p)
print()


n, k = map(int, input().split())
abilities = list(map(int, input().split()))
from math import comb

# 计算每个人单独赢得所有比赛的概率
p = [1.0] * n
q = [1.0] * n
win_prob = [1.0] * n
for i in range(n):
    for j in range(n):
        if i != j:
            win_prob[i] *= abilities[i] / (abilities[i] + abilities[j])
            p[i] *= abilities[i]
            q[i] *= (abilities[i] + abilities[j])

# 计算恰好 k 个人获胜的总概率
total_probability = 0.0
b = 1.0
for c in q:
    b *= c
# print(b)
# 遍历所有可能的获胜者组合
from itertools import combinations
for winners in combinations(range(n), k):
    # 计算这个组合的获胜概率
    prob = 1.0
    for i in range(n):
        if i in winners:
            prob *= p[i]
        else:
            prob *= q[i] - p[i]
    total_probability += prob
print(total_probability)
print(b)

print(total_probability / b)
