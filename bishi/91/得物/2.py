n, k = map(int, input().split())
s = list(input())
from collections import *
d = defaultdict(list)
last = 0
cur = 0
for i, c in enumerate(s):
    if i == 0:
        continue
    if c != s[i - 1]:
        d[s[i - 1]].append((last, i - 1))
        last = i
d[s[-1]].append((last, n - 1))
ans = float('-inf')
for c in d:
    cur = 0
    for l, r in d[c]:
        cur += (r - l + 1) // k
    ans = max(ans, cur)
print(ans)