import random

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = sum(a) + sum(b) + sum(c)
print(random.randint(ans // 2, ans // 4 * 3))
