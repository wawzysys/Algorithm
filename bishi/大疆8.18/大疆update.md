## 大疆后端B卷
一块地用一个从0开始素引的二维二送制矩阵block表示，其中0表示空闲地块，1表示放有障碍物购地块。在每个测试毛列中，地的左上角永远是空闲的。一架无人机面面向右侧侧，在左上角开造巡逻。
无人机将一直前进，直到抵达地的边界或遇到障碍物地时，无人机将会顺时针旋转90度并重复以上步，初始位置和无人机飞过的地块都会被之巡逻。
若无人机可以持续飞行下去，将返回被巡逻到的地块数量

输入
```
3 3
0 0 0 
1 1 0
0 0 0 
```
输出 
`
7
`
思路：
1. 初始化
创建一个bool的三维数组 vis 来标记是否被访问了四次不同的方向。
创建一个bool的二维数组 vis1 来标记每个地块是否已经被巡逻过，以避免重复计数。
设定初始位置 (x, y) = (0, 0)，并将其标记为已访问。
初始化方向向量 dx 和 dy 来表示无人机的四个可能移动方向（东、南、西、北），这些方向可以用一个索引 direction 来调控。
1. 模拟无人机移动
使用一个循环来模拟无人机的移动，直到它无法继续前进为止。
在每次循环中，先尝试移动到下一个位置 (X, Y)。
检查 (X, Y) 是否越界或为障碍物。如果是，更新 direction 来改变无人机的前进方向。
如果新方向仍不可行（即下一个位置依然越界或为障碍物），则跳出循环，表示无人机无法继续移动。
1. 方向更新与边界处理
每次无人机无法按当前方向前进时，顺时针旋转到下一个方向。
使用模 4 运算 ((direction + 1) % 4) 来简便地管理这四个方向的切换。
1. 计数与返回
记录无人机访问过的不重复地块数量。
最终，返回总的巡逻过的地块数量。
1. 结束算法
当所有的移动尝试都被障碍物或边界阻挡时，算法结束，返回计数结果。

### Tips：数据比较弱，只用一个二维vis1数组即可也可以100%

```java
public int numberOfPatrolBlocks2(int[][] grid) {
    if (grid == null || grid.length == 0 || grid[0].length == 0) {
        return 0;
    }

    Map<Integer, Integer> dx = new HashMap<>();
    Map<Integer, Integer> dy = new HashMap<>();

    dx.put(0, 0);
    dy.put(0, 1); // 向东
    dx.put(1, 1);
    dy.put(1, 0); // 向南
    dx.put(2, 0);
    dy.put(2, -1); // 向西
    dx.put(3, -1);
    dy.put(3, 0); // 向北

    int direction = 0;
    int m = grid.length;
    int n = grid[0].length;
    boolean[][][] vis = new boolean[m][n][4];
    boolean[][] vis1 = new boolean[m][n];
    int x = 0, y = 0;
    int patrolCount = 0;
    while (true) {
        if (!vis[x][y][direction]) {//四个方向
            vis[x][y][direction] = true;
            if (!vis1[x][y]) {//第一次访问
                vis1[x][y] = true;
                patrolCount++;
            }
        }
        int nextX = x + dx.get(direction);
        int nextY = y + dy.get(direction);
        if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1) {

            direction = (direction + 1) % 4;
            nextX = x + dx.get(direction);
            nextY = y + dy.get(direction);
            if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || grid[nextX][nextY] == 1
                    || vis[nextX][nextY][direction]) {
                break;
            }
        }
        x = nextX;
        y = nextY;
    }
    return patrolCount;
}
```