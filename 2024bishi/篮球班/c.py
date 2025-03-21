#C题
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x, y):
        x, y = self.find(x), self.find(y)
        return x == y
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] - 1
ds = DSU(n)
for i in range(n):
    ds.union(i, a[i])
ans = -1
for i in range(n):
    ds.find(i)
if ds.setCount == 1:
    ans = n
else:
    for i in range(n):
        tep = [max(i - 1, 0), min(i + 1, n - 1)]
        for j in tep:
            if not ds.connected(i, j):
                ans = max(ans, ds.size[ds.find(i)] + ds.size[ds.find(j)])
            
print(ans)      