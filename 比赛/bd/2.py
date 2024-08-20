
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
# from math import inf,sqrt,gcd,pow,ceil,floor,log,log2,log10,pi,sin,cos,tan,asin,acos,atan
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
n = sint()
c = 0;
dic = defaultdict(int)
for i in range(n):
    x, b = input().split()
    x = int(x)
    if b == 'R':
        dic[c] += 1
        dic[c + x] -= 1
        c = c +  x - 1
    else:
        dic[c - x + 1] += 1
        dic[c + 1] -= 1
        c = c - x + 1
nums = []
tep = sorted(dic.items())
for pr in tep:
    nums.append(pr)
n = len(nums)
answer = 0
sum = 0
for i in range(n):
    sum += nums[i][1]
    if sum % 4 == 1:
        answer = answer + nums[i + 1][0] - nums[i][0]
print(answer)