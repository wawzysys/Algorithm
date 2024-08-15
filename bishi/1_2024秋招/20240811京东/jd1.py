from collections import *
def count_pairs(a, X):
    c = defaultdict(int)
    ans = 0
    for i in a:
        c[i] += 1
        ans += c[X - i]
    ans = ans * 2
    if X % 2 == 0:
        ans -= c[X // 2]
    return ans
n, X = map(int, input().split())
a = list(map(int, input().split()))
print(count_pairs(a, X))
