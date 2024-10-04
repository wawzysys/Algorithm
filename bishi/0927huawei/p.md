# 1
公司组织绩效互评，为了避免有同学或者同团队的人互相打高分，需要将员工分成两组分别打分。给定一个整数n和一个数组GoodRelationships[]，其中，n表示人数，数组GoodRelationShips[]是一个邻接表GoodRelationShips[i]的元素[a,b,c]代表员工i和员工a，b，c是同学或者同团队。
请将这 n个人分成两组，使其每组不再有同学或者同团队的人。
GoodRelationShips[]的长度范围为[1,100]。
GoodRelationShips[i]中的元素的范围为[0,GoodRelationShips.length - 1]
GoodRelationShips[i]不会包含i或者有重复的值。
图是无向的: 如果j 在 GoodRelationships[i]里边,那么i也会在GoodRelationShips[]里边。

输入：
数组形式的员工关系邻接表，第一行数字代表有N个顶点，顶点编号从0开始，后续接N行。第i行代表第i-1个顶点和他有关系的同学的顶点编号

输出：
分组方案按照节点编号从小到大排序，如两个方案第一个节点相同，则按照第二个节点排序，以此类推;方案内部也按照编号从小到大排序。输出排序最靠前的一种方案，如无法分成符合条件的两组，则输出-1如输出如下两种方案时，选择第一种方案，因为方案一的分组2第一个节点编号更小:
分组1:1
分组2:2 3 4 5
和
分组1:1 2
分组2:3 4 5
如输出如下两种方案时，选择第二种方案，因为方案二的分组2第一个节点编号更小:
分组1:1 2
分组2:3 4 5
和
分组1:1 3
分组2:2 4 5

样例1：
输入：
4
1 3
0 2
1 3
0 2
输出：
0 2
1 3

解释：
我们可以将节点分成两组:{0,2}和{1，3}。

样例2：
输入：
4
1 2 3
0 2
0 1 2
0 2
输出：
-1

解释：
我们不能将节点分割成两个独立的子集

思路：
我们将员工关系建模为无向图，每个员工对应一个节点，关系对应边。通过广度优先搜索（BFS）对图进行二染色，尝试将节点分为两组，确保相邻节点颜色不同。如果在染色过程中发现相邻节点颜色相同，则说明图不是二分图，无法满足分组要求，输出 -1。如果成功染色，则根据颜色将员工分为两组，并对每组中的员工编号进行排序，最后选择字典序最小的分组方案输出。
```java
import java.util.*;

public class Bipartition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            System.out.println("-1");
            return;
        }
        int n = sc.nextInt();
        sc.nextLine();

        List<List<Integer>> g = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            String line = sc.hasNextLine() ? sc.nextLine().trim() : "";
            List<Integer> lst = new ArrayList<>();
            if(!line.isEmpty()) {
                String[] parts = line.split("\\s+");
                for(String p : parts) {
                    if(!p.isEmpty()) {
                        lst.add(Integer.parseInt(p));
                    }
                }
            }
            g.add(lst);
        }

        int[] col = new int[n];
        Arrays.fill(col, -1);
        boolean bip = true;

        List<Integer> g1 = new ArrayList<>();
        List<Integer> g2 = new ArrayList<>();

        for(int i = 0; i < n && bip; i++) {
            if(col[i] == -1) {
                Queue<Integer> q = new LinkedList<>();
                q.offer(i);
                col[i] = 0;
                List<Integer> comp = new ArrayList<>();
                comp.add(i);
                boolean valid = true;

                while(!q.isEmpty() && valid) {
                    int u = q.poll();
                    for(int v : g.get(u)) {
                        if(col[v] == -1) {
                            col[v] = col[u] ^ 1;
                            q.offer(v);
                            comp.add(v);
                        }
                        else if(col[v] == col[u]) {
                            valid = false;
                            break;
                        }
                    }
                }

                if(!valid) {
                    bip = false;
                    break;
                }

                int min = Collections.min(comp);
                if(col[min] == 1) {
                    for(int node : comp) {
                        col[node] ^= 1;
                    }
                }
            }
        }

        if(!bip) {
            System.out.println("-1");
            return;
        }

        for(int i = 0; i < n; i++) {
            if(col[i] == 0) g1.add(i);
            else g2.add(i);
        }

        Collections.sort(g1);
        Collections.sort(g2);

        if(compare(g1, g2) > 0) {
            System.out.println(toStr(g2));
            System.out.println(toStr(g1));
        }
        else {
            System.out.println(toStr(g1));
            System.out.println(toStr(g2));
        }
    }

    private static String toStr(List<Integer> list) {
        if(list.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < list.size(); i++) {
            if(i > 0) sb.append(" ");
            sb.append(list.get(i));
        }
        return sb.toString();
    }
    private static int compare(List<Integer> a, List<Integer> b) {
        int len = Math.min(a.size(), b.size());
        for(int i = 0; i < len; i++) {
            if(a.get(i) < b.get(i)) return -1;
            if(a.get(i) > b.get(i)) return 1;
        }
        if(a.size() < b.size()) return -1;
        if(a.size() > b.size()) return 1;
        return 0;
    }
}

```
# 2
小王是一名环保爱好者，每天选择乘坐公交车上班。不同线路上的公交车会在规定的路线上单向循环行驶，例如708路公交的路线为[2，5，8]，那么公交车会按照2->5->8->2->5->8->..的路线循环行驶，其中路线中的数字为公交站台编号。
小王每天上班会从离他家里最近的公交站台上车，然后在他最喜欢的早餐店所在的站台下车买好早餐然后再上车，最后在离公司最近的公交站台下车，允许不限次数地在中途下车换乘其他路线的公交现在分别给定小王上车、早餐店、下车的公交站台编号，请帮他选择最佳的乘车路线，使乘坐的公交车总数最少(如果在同1条公交路线中下车再上车，仍然视为乘坐的同一辆车)，从而获得最好的通体验。

输入
1.第一行有3个数字，分别表示上车的公交站台编号、早餐店的公交站台编号、下车公交站台编号，依次用空格隔开。
2.第二行表示公交路线数量，后续的每一行中第1个数字代表该路线的总站台数，剩余的数字表示每条公交路线经过的站点编号，所有数字用空格隔开。
3.公交路线数量范围在[1,500]。
4.公交站台的编号范围在[1,1000000]。5.每条公交路线经过的站台数量范围在[2,1500]，路线中的站台编号按升序顺序排序，且每条路线中不包含重复的站台。
6.起点站台、购买早餐的站点、终点站台不重复.

输出
乘坐的公交路线总数，如果没有匹配的路线请返回-1

样例1
输入
1 3 5
4
3 1 2 6
3 2 3 7
3 5 6 8
2 5 7

输出
3

解释：先乘坐第1条公交路线的车，在第2个站点下车转第2条路线的公交车，然后再乘坐第2条公交路线的车在站点3下车买早餐，然后重新乘坐第2条公交路线达到站点7下车转第4条公交路线，最后达到站点5，经过的公交路线为1->2->4，所以结果为3。虽然乘坐第1条公交路线和第3条公交路线也能达到站点5，但是该路线没法购买早餐。

样例2
输入
1 3 4
2
3 1 2 4
3 3 5 6

输出
-1
解释
小王只能乘坐第1条公交路线上车，但是无法通过该路线的站台换乘到第2条公交路线购买早餐，没有匹配的路线，返回-1。

样例3
输入
4 19 28
5
5 3 4 7 8 10
6 10 12 16 19 27 28
4 5 7 11 17
4 17 19 22 23
3 23 27 28
输出
2
解释:小王可以选择1->2的公交路线，乘坐的公交车总数为2，也可以选择1->3->4->5的公交路线，乘坐的公交车总数为4，因此最佳的乘车路线是1->2，结果为2。

思路：
构建关系图：利用 graph 记录每个站台经过的所有公交线路，并初始化 dp 数组表示从 b 出发到达各条公交线路的最小乘车次数。

广度优先搜索（BFS）：从 b 所在站台的公交线路出发，遍历所有可能的换乘路径，更新 dp 数组。

计算结果：遍历 a 和 c 所在站台对应的公交线路，求解从 a 到 b 再到 c 的最小乘车次数。

```cpp
#include <bits/stdc++.h>
using namespace std;
void solve() {
    int a, b, c, n;
    cin >> a >> b >> c >> n;

    long long inf = 1e18;
    vector<long long> dp(n, inf);
    unordered_map<int, vector<int>> graph;
    vector<vector<int>> st(n);

    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        st[i].resize(k);
        for (int j = 0; j < k; ++j) {
            cin >> st[i][j];
            graph[st[i][j]].push_back(i);
        }
    }

    queue<int> q;
    for (int idx : graph[b]) {
        dp[idx] = 0;
        q.push(idx);
    }

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int u : st[cur]) {
            for (int v : graph[u]) {
                if (dp[v] > dp[cur] + 1) {
                    dp[v] = dp[cur] + 1;
                    q.push(v);
                }
            }
        }
    }

    long long t1 = inf, t2 = inf;
    for (int idx : graph[a]) t1 = min(t1, dp[idx]);
    for (int idx : graph[c]) t2 = min(t2, dp[idx]);

    if (t1 + t2 > inf) {
        cout << -1 << endl;
    } else {
        cout << t1 + t2 + 1 << endl;
    }
}

int main() {
    solve();
    return 0;
}
```

# 3
最近病毒肆虐，科学家为了研究病毒的传播轨迹，需要设计一套简易的传播模型。
在一张M*N地图中，包含墙体，空地，已感染的人(不戴口罩)，已感染的人(戴口罩)，未感染的人(不戴口罩)，未感染的人(戴口罩)。科学家会设置一些危险系数，以及感染阈值。然后观察未感染人群大概多少天以后会被感染。
位置含义的编码如下:

数值：
0 空地
1 墙壁
2 已感染的人(不戴口罩)
3 已感染的人(戴口罩)
4 未感染的人(不戴口罩)
5 未感染的人(戴口罩)

危险系数:为感染的人对周围的位置造成的风险(戴口罩和不戴口罩数值不同)，每过一格，危险系数就减1。遇到墙体则不再进行传播。一个位置上如果出现多个传染源传播的危险系数，则危险系数使用多个危险系数的最大值.感染阈值:为该位置的人被感染的门限(戴口罩和不戴口罩数值不同)当危险系数大于等于感染阈值，则该位置的人就会被传染。

感染阈值:为该位置的人被感染的门限(戴口罩和不戴口罩数值不同)当危险系数大于等于感染阈值，则该位置的人就会被传染。
注意:1.判断当前位置是否感染只有一个条件，就是当前位置上的危险系数是否大于等于当前位置上的人的感染阈值。是否带口罩会影响危险系数和感染阈值的大小，从而间接的影响该位置的人是否会被感染，2.未感染的人在感染后会在第二天变成已感染的人，比如未感染的人(戴口罩)如果在第3天发现自己的感染阈值小于危险系数(也就是会被感染)，那么在第4天该位置就会变成已感染的人(戴口罩).所以在第4天以后需要将该位置以及周围的危险系数刷新，这就有可能会感染其他更多的人。

输入
第一行: M, N, a1,a2,b1,b2 用空格隔开，参数具体含义如下:
M 地图行信息 1<=M<=100
N 地图列信息 1 <= N <= 100
a1 危险系数(戴口罩) 1<=a1 <a2 <= 1000
a2 危险系数(不戴口罩) 1 <= a1 <a2 <= 1000
b1 感染阈值(戴口罩)   1<= b2<b1 <= 1000
b2 感染阈值(不戴口罩)  1<= b2<b1 <= 1000
第二行到第M+2行: M行N列地图数据信息

输出
输出M行N列数据信息，每个位置需要输出的内容如下:
该位置没有人(空地或者墙壁)的话则返回-1
该位置的人初始态时就被感染了的话，则填0
该位置的人初始没有被感染，但是最终被感染，则填被感染的天数该位置的人没有被感染，则返回-1

样例1：
输入：
3 4 7 10 6 2
0 0 0 0 
2 0 1 5
0 0 0 0
输出：
-1 -1 -1 -1
0 -1 -1 -1
-1 -1 -1 -1

样例2：
输入：
3 4 7 10 6 2
0 0 0 0
2 0 1 5
0 0 0 5
输出：
-1 -1 -1 -1
0 -1 -1 2
-1 -1 -1 1

解释:该用例中，初始地图中，第2行第1列处存在一个已感染并且不戴口罩的人，根据危险系数的配置信息，危险系数(不戴口罩)为10，所以该位置的危险系数为10，计算所有位置的危险系数如下:
9 8 7 6
10 9 - 5
9 8 7 6

第2行第4列位置上的危险系数为5，该位置上的人戴了口罩，该位置上的人感染阈值为6，则该人在第一天不会被感染，第3行第4列位置上的危险系数为6，该位置上的人戴了口罩，该位置上的人感染阈值为6，则该人在第一天会被感染。感染后该人会变成已感染的人(戴口罩)

第一天以后地图更新如下:
0 0 0 0
2 0 1 5
0 0 0 3
这时再计算第二天的危险系数，根据危险系数的配置信息，危险系数(戴口罩)为7，所以第3行第4列位置的危险系数为7，所有位置需要计算危险系数的最大值，如下图。
(9,2)=9   (8,3)=8  (7,4)=7   (6,5)=6  
(*10,3)=10  (9,4)= 9  -      (5,6)=6 
(9,4)= 9  (8,5)= 8   (7,6)=7   (6,*7)=7
第二天，第2行第4列位置上的危险系数从5提升到了6，而该位置上的人感染阈值为6，则该位置的人会在第二天被感染。
最终结果如下:
-1 -1 -1 -1
0 -1 -1 2
-1 -1 -1 1


思路：
构建二维数组 g 表示地图状态，并初始化感染天数数组 d 和初始感染源列表 inf。
传播危险系数：
使用优先队列按危险系数从大到小传播，遇到墙壁或危险系数小于等于 0 则停止传播。
更新未感染位置的危险系数。
感染判断与状态更新：
判断未感染位置的危险系数是否达到感染阈值，满足条件则记录感染天数，并将该位置加入新感染源列表。
重复传播与感染：
循环进行传播和感染判断，直至没有新的感染源（即传播结束）。
输出结果：
根据 d 数组输出每个位置的感染天数或 -1（未感染或障碍物）。
```java
import java.util.*;

public class Main {
    static class Node {
        int x, y, danger;

        Node(int x, int y, int danger) {
            this.x = x;
            this.y = y;
            this.danger = danger;
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int M = s.nextInt(), N = s.nextInt();
        int a1 = s.nextInt(), a2 = s.nextInt();
        int b1 = s.nextInt(), b2 = s.nextInt();
        int[][] g = new int[M][N];
        int[][] d = new int[M][N];
        List<int[]> inf = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                g[i][j] = s.nextInt();
                if (g[i][j] == 2 || g[i][j] == 3) {
                    d[i][j] = 0;
                    inf.add(new int[]{i, j});
                } else {
                    d[i][j] = -1;
                }
            }
        }
        int day = 0;
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        while (!inf.isEmpty()) {
            day++;
            int[][] D = new int[M][N];
            for (int[] row : D) Arrays.fill(row, 0);
            PriorityQueue<Node> q = new PriorityQueue<>((n1, n2) -> n2.danger - n1.danger);
            for (int[] p : inf) {
                int x = p[0], y = p[1];
                int danger = (g[x][y] == 2) ? a2 : a1;
                q.offer(new Node(x, y, danger));
                D[x][y] = danger;
            }
            while (!q.isEmpty()) {
                Node n = q.poll();
                int x = n.x, y = n.y, danger = n.danger;
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k], ny = y + dy[k];
                    if (nx >= 0 && nx < M && ny >= 0 && ny < N && g[nx][ny] != 1) {
                        int nd = danger - 1;
                        if (nd > 0 && D[nx][ny] < nd) {
                            D[nx][ny] = nd;
                            q.offer(new Node(nx, ny, nd));
                        }
                    }
                }
            }
            List<int[]> newInf = new ArrayList<>();
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < N; j++) {
                    if ((g[i][j] == 4 || g[i][j] == 5) && d[i][j] == -1) {
                        int th = (g[i][j] == 4) ? b2 : b1;
                        if (D[i][j] >= th) {
                            d[i][j] = day;
                            newInf.add(new int[]{i, j});
                        }
                    }
                }
            }
            for (int[] p : newInf) {
                int x = p[0], y = p[1];
                if (g[x][y] == 4) g[x][y] = 2;
                else if (g[x][y] == 5) g[x][y] = 3;
            }
            inf = newInf;
        }
        for (int i = 0; i < M; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < N; j++) {
                int res;
                if (g[i][j] == 0 || g[i][j] == 1) res = -1;
                else res = d[i][j];
                sb.append(res).append(j == N - 1 ? "" : " ");
            }
            System.out.println(sb.toString());
        }
    }
}

```