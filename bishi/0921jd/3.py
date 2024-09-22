import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def main():
    n = sint()
    colors = lint()
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = mint()
        adj[x].append(y)
        adj[y].append(x)
    parent = [0]*(n+1)
    children = [[] for _ in range(n+1)]
    q = deque()
    root =1
    parent[root]=0
    q.append(root)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v != parent[u]:
                parent[v]=u
                children[u].append(v)
                q.append(v)
    max_xor =0
    def dfs(u):
        nonlocal max_xor
        freq = defaultdict(int)
        freq[colors[u-1]] +=1
        for v in children[u]:
            child_freq = dfs(v)
            for c, cnt in child_freq.items():
                freq[c] +=cnt
        current_max_freq = max(freq.values())
        colors_to_remove = set()
        for c, cnt in freq.items():
            if cnt == current_max_freq:
                colors_to_remove.add(c)
        xor_val =0
        for c, cnt in freq.items():
            if c not in colors_to_remove:
                if cnt %2 ==1:
                    xor_val ^=c
        if xor_val > max_xor:
            max_xor = xor_val
        return freq
    dfs(root)
    print(max_xor)
if __name__ == "__main__":
    main()
