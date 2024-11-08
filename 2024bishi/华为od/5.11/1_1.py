from collections import *
inf = float('inf')
dict = defaultdict(lambda : [inf, -inf, inf, -inf])

m, n = map(int, input().split())

for i in range(m):
    nums = list(map(int, input().split()))
    for j, num in enumerate(nums):
        if num > 0:
            dict[num][0] = min(dict[num][0], i)
            dict[num][1] = max(dict[num][1], i)
            dict[num][2] = min(dict[num][2], j)
            dict[num][3] = max(dict[num][3], j)
ans = 0

for num in dict:
    ans = max(ans, (dict[num][1] - dict[num][0] + 1) * (dict[num][3] - dict[num][2] + 1))
print(ans)