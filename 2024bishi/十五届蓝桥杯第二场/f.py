import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def main():
    n, m = map(int, input().split())
    caves = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    
    for _ in range(m):
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        distances = dijkstra(graph, s)
        print(distances[t])

if __name__ == "__main__":
    main()
