sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
from collections import deque
n = sint()
d = [0] + lint()
a = [[] for _ in range(n+1)]
idg = [0]*(n+1)
for i in range(1, n+1):
    line = input().strip()
    if line == "-1" or not line:
        continue
    deps = list(map(int, line.split()))
    for num in deps:
        a[num].append(i)
        idg[i] +=1
q = deque()
e = [0]*(n+1)
for j in range(1, n+1):
    if idg[j]==0:
        q.append(j)
        e[j]=d[j]
while q:
    u = q.popleft()
    for v in a[u]:
        if e[u] + d[v] > e[v]:
            e[v] = e[u] + d[v]
        idg[v] -=1
        if idg[v]==0:
            q.append(v)
print(max(e))
