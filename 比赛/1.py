from collections import deque

N, M, K = map(int, input().split())
adj = {}
for _ in range(N):
    X, Y = map(int, input().split())
    adj.setdefault(X, []).append(Y)
    adj.setdefault(Y, []).append(X)

visited = set()
queue = deque()
visited.add(M)
queue.append((M, 0))

while queue:
    node, depth = queue.popleft()
    if depth >= K:
        continue
    for neighbor in adj.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, depth + 1))

print(len(visited) - 1)  
