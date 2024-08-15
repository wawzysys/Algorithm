from collections import *
nums = [0, 25, 21, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
N = int(input())
ss = defaultdict(int)
for _ in range(N):
    for _ in range(20):
        a, b = map(int, input().split())
        if b > len(nums):
            print('1')
        ss[a] -= nums[b]

ans = []
for c in ss:
    ans.append([ss[c], c])
ans.sort()
for a, b in ans:
    print(b, -a)
