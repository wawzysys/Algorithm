from collections import *
n = int(input())
nums = list(map(int, input().split()))
ans = 0
m = int(input())
mo = defaultdict(int)
for c in nums:
    mo[c % m] += 1
    ans = max(ans, mo[c % m])
nums.sort()
# print(nums)
for c in nums:
    if mo[c % m] == ans:
        print(c)
        break