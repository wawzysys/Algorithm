import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1000000)
    n, b = map(int, sys.stdin.readline().split())
    c = []
    d = []
    x = []
    children = [[] for _ in range(n)]
    for i in range(n):
        parts = sys.stdin.readline().split()
        if i == 0:
            ci, di = map(int, parts)
            c.append(ci)
            d.append(di)
        else:
            ci, di, xi = map(int, parts)
            c.append(ci)
            d.append(di)
            children[xi-1].append(i)  # xi是1-based

    # 修正后的 Find roots
    has_parent = [False]*n
    for i in range(n):  # 从0开始
        for child in children[i]:
            has_parent[child] = True
    roots = [i for i in range(n) if not has_parent[i]]

    from collections import defaultdict

    def merge_lists(l1, l2):
        result = {}
        for k1, c1 in l1:
            for k2, c2 in l2:
                k = k1 + k2
                cost = c1 + c2
                if k not in result or cost < result[k]:
                    result[k] = cost
        # Convert to sorted list
        merged = sorted(result.items())
        # Remove dominated entries
        optimized = []
        min_cost = float('inf')
        for k, cost in merged:
            if cost < min_cost:
                optimized.append((k, cost))
                min_cost = cost
        return optimized

    def tree_dp(u):
        # Base case: no children
        dp0 = [(0, 0)]
        dp1 = [(1, c[u])]
        dp2 = [(1, c[u] - d[u])]
        for v in children[u]:
            child_dp0, child_dp1, child_dp2 = tree_dp(v)
            # 对于不购买当前节点的情况，只能选择不购买子节点
            # 对于购买当前节点的情况，可以选择购买子节点或不购买
            # 这里需要合并不同的状态
            # 更新dp0
            options0 = child_dp0 + child_dp1  # 不强制购买子节点
            dp0 = merge_lists(dp0, options0)
            # 更新dp1
            options1 = child_dp0 + child_dp1
            dp1 = merge_lists(dp1, options1)
            # 更新dp2
            options2 = child_dp0 + child_dp1 + child_dp2
            dp2 = merge_lists(dp2, options2)
        return dp0, dp1, dp2

    # Collect all tree options
    all_options = []
    for r in roots:
        dp0, dp1, dp2 = tree_dp(r)
        # 合并所有状态
        tree_options = {}
        for dp in [dp0, dp1, dp2]:
            for k, cost in dp:
                if k not in tree_options or cost < tree_options[k]:
                    tree_options[k] = cost
        # Convert to sorted list
        sorted_options = sorted(tree_options.items())
        # Remove dominated entries
        optimized = []
        min_cost = float('inf')
        for k, cost in sorted_options:
            if cost < min_cost:
                optimized.append((k, cost))
                min_cost = cost
        all_options.append(optimized)

    # Global DP
    dp_global = [float('inf')] * (n + 1)
    dp_global[0] = 0
    for tree in all_options:
        new_dp = [float('inf')] * (n + 1)
        for k1 in range(n + 1):
            if dp_global[k1] <= b:
                for k2, c2 in tree:
                    if k1 + k2 > n:
                        continue
                    if dp_global[k1] + c2 < new_dp[k1 + k2]:
                        new_dp[k1 + k2] = dp_global[k1] + c2
        for k in range(n + 1):
            if new_dp[k] < dp_global[k]:
                dp_global[k] = new_dp[k]
    # Find the maximum k with dp_global[k] <= b
    max_k = 0
    for k in range(n + 1):
        if dp_global[k] <= b:
            max_k = k
    print(max_k)

threading.Thread(target=main,).start()
