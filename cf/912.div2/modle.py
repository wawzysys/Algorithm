class Node:
    __slots__ = "l", "r", "mid", "val", "left", "right"

    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.val = -1  # 结点维护信息
        self.laze = None  # 懒标记
        self.left = None
        self.right = None


def pushUp(node: Node):
    node.val = max(node.left.val, node.right.val)


def pushDown(node: Node):
    if node.left is None:
        node.left = Node(node.l, node.mid)
    if node.right is None:
        node.right = Node(node.mid + 1, node.r)
    # 实现 lazy

class Seg:
    def __init__(self):
        self.root = Node(0, int(1e9))

    def update(self, x, val, node: 'Node' = None):
        if node is None:
            node = self.root
        if node.l == x and node.r == x:
            node.val = max(node.val, val)
            return
        pushDown(node)
        if x <= node.mid:
            self.update(x, val, node.left)
        else:
            self.update(x, val, node.right)
        pushUp(node)

    def query(self, l, r, node: 'Node' = None):
        if node is None:
            node = self.root
        if l <= node.l and node.r <= r:
            return node.val
        pushDown(node)
        ans = -1
        if l <= node.mid:
            ans = max(ans, self.query(l, r, node.left))
        if r > node.mid:
            ans = max(ans, self.query(l, r, node.right))
        return ans


class FenWick:
    def __init__(self, n: int):
        self.n = n
        self.tr = [0 for _ in range(n + 1)]

    def sum(self, i: int):
        i += 1
        s = 0
        while i >= 1:
            s += self.tr[i]
            i &= i - 1
        return s

    def rangeSum(self, l: int, r: int):
        return self.sum(r) - self.sum(l - 1)

    def add(self, i: int, val: int):
        i += 1
        while i <= self.n:
            self.tr[i] += val
            i += i & -i