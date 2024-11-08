
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
nums = [sint() for _ in range(n)]
nums2 = sorted(nums)
dic = defaultdict(int)
for i, c in enumerate(nums2):
    dic[c] = i
s = 0
for i, c in enumerate(nums):
    if i % 2 != dic[c] % 2:
        s += 1
print(s // 2)


