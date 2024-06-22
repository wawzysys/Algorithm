import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

n, m, nq = mii()
weights = lii()
g = [[] for _ in range(n)]
edges = []
for _ in range(m):
    u, v = mii()
    u -= 1; v -= 1
    edges.append((u, v))

keep = [True] * m
queries = []
for _ in range(nq):
    tp, *q = mii()
    if tp == 1:
        k = q[0] - 1
        keep[k] = False
        queries.append((1, k))
    else:
        queries.append((2, *q))
queries.reverse()

parent = list(range(n))
mps = [{weights[u]: 1} for u in range(n)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru == rv:
        return
    if len(mps[ru]) < len(mps[rv]):
        ru, rv = rv, ru
    parent[rv] = ru
    for kv, vv in mps[rv].items():
        mps[ru][kv] = mps[ru].get(kv, 0) + vv

for st, (u, v) in zip(keep, edges):
    if st:
        g[u].append(v)
        g[v].append(u)
        union(u, v)

ans = []
for tp, *q in queries:
    if tp == 1:
        k = q[0]
        union(*edges[k])
    else:
        u, target = q
        target -= weights[u]
        res = mps[find(u)].get(target, 0)
        if target == weights[u]:
            res -= 1
        ans.append(res)

ans.reverse()
print(*ans, sep='\n')

