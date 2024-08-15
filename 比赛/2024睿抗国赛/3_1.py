# a = 125
# b = 251
# c = 512

# ans1 = a * a + b * b + c * c
# ans2 = d * d + e * e + f * f
# 是ans1 = ans2这样的相等
from collections import deque
# print(ans1, ans2)  
n = int(input())
nums = list(map(int, input().split()))
q = deque()
for c in nums:
    q.append(str(c))
print(''.join(q))
for _ in range(n - 1):
    q.append(q[0])
    q.popleft()
    print(''.join(q))
