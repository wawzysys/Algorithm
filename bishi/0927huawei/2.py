from collections import deque, defaultdict
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    a = sint()
    b, c, n = mint()
    
    INF = 10**18
    dp = [INF] * n
    graph = defaultdict(list)  
    st = [[] for _ in range(n)]  
    
    for i in range(n):
        inputs = lint()
        if not inputs:
            inputs = lint()
        k = inputs[0]
        keys = inputs[1:]
        if len(keys) < k:
            while len(keys) < k:
                keys += lint()
        st[i].extend(keys[:k])
        for key in keys[:k]:
            graph[key].append(i)
    
    queue = deque()
    for idx in graph.get(b, []):
        if dp[idx] > 0:
            dp[idx] = 0
            queue.append(idx)
    
    while queue:
        current = queue.popleft()
        for key in st[current]:
            for neighbor in graph.get(key, []):
                if dp[neighbor] > dp[current] + 1:
                    dp[neighbor] = dp[current] + 1
                    queue.append(neighbor)
    
    t1 = min([dp[idx] for idx in graph.get(a, [])], default=INF)
    t2 = min([dp[idx] for idx in graph.get(c, [])], default=INF)
    
    if t1 == INF or t2 == INF:
        print(-1)
    else:
        print(t1 + t2 + 1)


solve()
