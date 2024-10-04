import sys, heapq
mint = lambda: map(int, input().split())
def main():
    n, m = mint()
    ts = set([1, n])
    edges = []
    for _ in range(m):
        u, v = mint()
        ts.add(u)
        ts.add(v)
        edges.append((u, v))
    lst = sorted(ts)
    d = {x:i for i,x in enumerate(lst)}
    graph = [[] for _ in range(len(lst))]
    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]
        graph[i].append((i+1, diff))
        graph[i+1].append((i, diff))
    for u, v in edges:
        graph[d[u]].append((d[v], 0))
        graph[d[v]].append((d[u], 0))
    start, end = d[1], d[n]
    dist = [1<<60]*len(lst)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if u == end:
            print(cost)
            return
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            if cost + w < dist[v]:
                dist[v] = cost + w
                heapq.heappush(heap, (dist[v], v))
    print(-1)

if __name__ == "__main__":
    main()
