lint = lambda: list(map(int, input().split()))
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]

def main():
    n = int(input())
    dsu = DSU(n)
    a = [0] + lint()
    for i in range(1, n + 1):
        x = a[i]
        dsu.union(i, x)

    ans = n
    for i in range(1, n + 1):
        if dsu.find(i) == i:
            ans += dsu.size[i] * (dsu.size[i] - 1)

    print(ans)

if __name__ == "__main__":
    main()
