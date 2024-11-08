# pdd手撕
def solve(V, E):
    # 构建图的邻接表表示
    graph = {v: [] for v in V}
    for edge in E:
        v1, v2 = edge
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 记录访问过的节点
    visited = set()

    # 深度优先遍历
    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    # 统计连通分量
    components_count = 0
    for node in V:
        if node not in visited:
            visited.add(node)
            dfs(node)
            components_count += 1
    
    return components_count

V = ['v1', 'v2', 'v3', 'v4']
E = [['v1', 'v2'], ['v3', 'v4']]
print(solve(V, E))  # 输出 2
