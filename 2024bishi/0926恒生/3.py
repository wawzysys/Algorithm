import heapq
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def min_cost(n, m, a, roads, s, t):
    graph = [[] for _ in range(n + 1)]  
    for u, v, l, w in roads:
        cost = a * l + w
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    
    while heap:
        current_cost, u = heapq.heappop(heap)

        if u == t:
            return current_cost
        if current_cost > dist[u]:
            continue
        
        for v, cost in graph[u]:
            new_cost = current_cost + cost
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    return -1

n, m, a = mint()

roads = []
for _ in range(m):
    u, v, l, w = mint()
    roads.append((u, v, l, w))
s, t = mint()
result = min_cost(n, m, a, roads, s, t)
print(result)
