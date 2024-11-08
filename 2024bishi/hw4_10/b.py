class DSU:
    def __init__(self, n):
        """
        初始化并查集。
        参数 n: 总共的节点数。
        """
        self.f = list(range(n))  # 初始化每个节点的父节点为自己
        self.siz = [1] * n       # 初始化每个节点所在集合的大小为1

    def find(self, x):
        """
        查找节点x的根节点，并进行路径压缩优化。
        """
        if x != self.f[x]:           # 路径压缩
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def same(self, x, y):
        """
        判断节点x和节点y是否属于同一个集合。
        """
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        """
        合并节点x和y所在的集合，采用按秩合并优化。
        返回值: 如果x和y已经在同一集合中则返回False，否则返回True。
        """
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        # 按秩合并
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.siz[x] += self.siz[y]
        self.f[y] = x
        return True

    def size(self, x):
        """
        返回节点x所在集合的大小。
        """
        return self.siz[self.find(x)]

def solve(n, a):
    """
    解决给定的问题，使用并查集分组后计算每组的互动值。
    
    参数:
    - n (int): 矩阵的大小。
    - a (list of list of int): 互动值矩阵。

    返回:
    - list: 每组的互动值总和，按从大到小排序。
    """
    uf = DSU(n)  # 创建并查集实例
    # 建立并查集关系
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                uf.merge(i, j)

    b = {}
    # 按根节点分组
    for i in range(n):
        root = uf.find(i)
        if root not in b:
            b[root] = []
        b[root].append(i)

    ans = []
    # 计算每组的互动值
    for v in b.values():
        res = 0
        for x in v:
            for y in v:
                res += a[x][y]
        res //= 2  # 由于互动值矩阵是对称的，所以每对互动值被计算了两次
        ans.append(res)

    ans.sort(reverse=True)  # 从大到小排序
    return ans

# 示例输入处理
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 调用solve函数并输出结果
print(*solve(n, a))
