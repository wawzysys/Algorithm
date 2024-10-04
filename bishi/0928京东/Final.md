### 京东后端开发工程师

---

### **第一题：猜数游戏**
#### 题意
一天，小A与小B进行猜数游戏，由小A在随机选择一个整数K并给出Q个提示，小B猜数。每次给出的提示中包含两个整数M,D--表示M与K的差的绝对值不超过D。现在，小B想根据小A给出的Q条提示找出满足提示的最大的K。

#### 输入描述
- 第一行包含一个整数Q，表示提示的条数 (1 <= Q <= 10^5)。
- 随后的Q行，每行给出两个整数M和D (0 <= M, D <= 10^9)。

#### 输出描述
输出满足提示的最大的整数K。如果没有这样的数，输出 -1。

#### 示例1：
输入：
```
3
3 3
2 5
5 3
```
输出：
```
6
```

#### 示例2：
输入：
```
3
1 1
2 2
3 3
```
输出：
```
2
```

#### 思路与代码
通过计算每对(M,D)所确定的K的范围 `[M-D, M+D]`，找到这些范围的交集。如果存在交集，输出交集的最大值，否则输出 -1。

```python
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
from collections import *
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    import sys
    Q,*rest = map(int, sys.stdin.read().split())
    L=-10**18
    U=10**18
    for i in range(0,2*Q,2):
        M,D=rest[i],rest[i+1]
        L=max(L, M-D)
        U=min(U, M+D)
    print(U if L<=U else -1)
    
if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    solve()

```

---

### **第二题：正方体三视图**
#### 题意
“学霸题，数正方体，头顶标数法，三层标上3，二层标上2，一层标上1，全部加起来，你学会了吗”
给定一个矩阵，矩阵中的每个数字表示这个位置上叠放的小正方体数量。小正方体边长为1。
请问:题目所描述的几何体的三视图(从正面、左面和上方看的投影)各白的面积为参多少？

#### 输入描述
- 第一行两个整数n和m，表示矩阵的行数和列数 (1 ≤ n, m ≤ 100)。
- 随后的n行，每行m个整数aij，表示该位置上叠放的小正方体数量 (0 ≤ aij ≤ 100)。

#### 输出描述
输出三视图的面积：从正面、左面和上面看的投影面积。

#### 示例1：
输入：
```
2 3
3 3 2
3 2 1
```
输出：
```
8 6 6
```

#### 思路与代码
- 正视图：每列的最大值之和。
- 左视图：每行的最大值之和。
- 俯视图：非零元素的个数。

```python
import sys
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def main():
    n, m = mint()
    a = [lint() for _ in range(n)]
    
    front = sum(max(col) for col in zip(*a))
    left = sum(max(row) for row in a)
    top = 0
    for i in a:
        for c in i:
            if c > 0:
                top += 1
    
    print(front, left, top)

if __name__ == "__main__":
    main()

```

---

### **第三题：牛牛的最短路问题**
#### 题意
在2077年牛牛所在的世界可以简化成一条数轴，牛牛在位置1上，而牛牛的目的地在n。牛牛的每分钟可以走一米，她每次可以选择往左走或往右走。在这条数轴上，还存在m个传送装置。每个装置连接着数轴上的两个点(u,v)，当牛牛走到具有装置的点u时，其可以选择传送到点v，v点同理且每次传送耗时为0。牛牛现在希望你能帮他规划一下路线使得其到达目的地的时间是最少的。


#### 输入描述
- 第一行为n, m，表示目的地坐标和传送装置的个数 
- 接下来有m行，每行为两个整数表示装置连接的两个点u, v (1 ≤ u, v ≤ n)。
1 ≤ n ≤ 10^9, 1 ≤ m ≤ 10^4, 1 ≤ u, v ≤ n
#### 输出描述
输出牛牛到达目的地的最少时间。

#### 示例1：
输入：
```
10 2
1 5
4 10
```
输出：
```
1
```

#### 思路与代码
使用集set 来去重并存储这些位置。
排序并建立索引：
将所有重要位置排序，存入列表 lst。
创建一个字典 d，将每个位置映射到其在排序列表中的索引。
初始化一个邻接表 graph，每个节点存储其相邻节点及对应的移动代价。
对于排序列表中的相邻位置，添加双向边，代价为两位置的差值（即步行时间）。
对于每个传送装置，添加双向边，代价为 0（传送不耗时）
然后Dijkstra求最短路
如果队列为空且未到达终点输出-1

```python
import sys, heapq
mint = lambda: map(int, input().split())
def main():
    n, m = mint()
    ts = set([1, n])
    edges = []
    for _ in range(m):
        u, v = mint()
        ts.add(u)
        ts.add(v)
        edges.append((u, v))
    lst = sorted(ts)
    d = {x:i for i,x in enumerate(lst)}
    graph = [[] for _ in range(len(lst))]
    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]
        graph[i].append((i+1, diff))
        graph[i+1].append((i, diff))
    for u, v in edges:
        graph[d[u]].append((d[v], 0))
        graph[d[v]].append((d[u], 0))
    start, end = d[1], d[n]
    dist = [1<<60]*len(lst)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if u == end:
            print(cost)
            return
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            if cost + w < dist[v]:
                dist[v] = cost + w
                heapq.heappush(heap, (dist[v], v))
    print(-1)

if __name__ == "__main__":
    main()

```