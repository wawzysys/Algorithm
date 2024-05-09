# 定义lambda表达式简化输入的读取和处理
input = lambda: sys.stdin.readline().rstrip()  # 读取一行输入并去除行尾空白字符
m_input = lambda: int(input())  # 读取一行输入并转换为整数
mint = lambda: map(int, input().split())  # 读取一行分割的多个整数
ints = lambda: list(map(int, input().split()))  # 将读取的整数转换为列表

# 主要的解决方案函数
def solve() -> None:
    n = int(input())  # 读取整数n
    a = [list(map(int, input().split())) for i in range(n)]  # 读取一个整数矩阵
    exposed = list(map(int, input().split()))  # 读取一个整数列表
    res = inf  # 初始化结果为无限大


    def bfs(x):
        nonlocal res  # 允许访问函数外的res变量
        ans = 0
        q = deque()  # 创建双端队列
        st = [False] * n  # 创建状态列表，记录节点是否访问过
        st[x] = True
        q.append((x, 10))  # 将起点和初始值加入队列
        while q:  # 当队列不为空时执行循环
            u, r = q.popleft()  # 从队列中取出一个元素
            for i in range(n):  # 遍历所有节点
                if a[u][i] <= r and not st[i]:  # 检查条件并确认节点未访问
                    q.append((i, r))  # 将符合条件的节点加入队列
                    st[i] = True  # 标记节点为已访问
                    ans += 1
        res = min(res, ans)  # 更新结果为最小值

    # 对每个需要检查的点执行BFS
    for x in exposed:
        bfs(x)
    print(res)  # 打印最终结果

if __name__ == '__main__':
    solve()