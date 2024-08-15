
from collections import *
from heapq import *
n, m, s, t = map(int, input().split())
re = [0] + list(map(int, input().split()))
mh = [0 for _ in range(n + 1)]
inf = float('inf')
dis = [inf for _ in range(n + 1)]
grape = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    grape[a].append([b, c])
    grape[b].append([a, c])
pq = [(0, s, 0)]
while pq:
    d, x, y = heappop(pq)
    if d > dis[x]:
        continue
    for i, j in grape[x]:
        if dis[i] > d + j:
            dis[i] = d + j
            heappush(pq, (d + j, i, max(y, re[i])))
if dis[t] == inf:
    print('Impossible')
else:
    print(dis[t], y)
