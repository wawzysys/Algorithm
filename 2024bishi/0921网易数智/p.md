# 1
小明家附近有两个购物超市A、B，两家超市中的商品种类都一致齐全,其中A超市离小明家更近，是小明购物的首选超市，但是B超市的有些商品会比A超市价格便宜，而且B超市有个购物规定，每次买东西只能选1件或多件相互挨着的商品，不能随意挑选。假设小明要采购一系列商品，每件只购买一次，只能在A或B超市中采购，并且他最多只去B超市采购一次，请你帮助计算本次采购全部商品清单所需的最低费用。

输入描述
输入包括两行，每行均为n个数字，用空格分隔，1<=n<10000000
第一行为本次需采购的n个商品在A超市的价格列表
第二行为本次需采购的n个商品在B超市的价格列表
第二行非0正整数，且小于100
输出：
最低费用
示例1：
输入:
36 87 47 55 51
39 77 46 57 50
输出
265

思路：
作差，D[i] = B[i] - A[i]
然后求D数组的最小连续子数组和 min
输出 sum(A) + min

```c++
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    string lineA;
    getline(cin, lineA);
    string lineB;
    getline(cin, lineB);
    vector<int> A;
    int num;
    ll sumA = 0;
    stringstream ssA(lineA);
    while (ssA >> num)
    {
        A.push_back(num);
        sumA += num;
    }

    stringstream ssB(lineB);
    ll min_s = 0;
    ll cur_s = 0;
    int i = 0;
    while (ssB >> num && i < A.size())
    {
        int D = num - A[i];
        cur_s += D;
        if (cur_s < min_s)
        {
            min_s = cur_s;
        }
        if (cur_s > 0)
        {
            cur_s = 0;
        }
        i++;
    }

    ll ans = sumA + min_s;
    if (min_s >= 0)
    {
        ans = sumA;
    }

    cout << ans;
}

```

# 2
有一座城市共有n个公交站点，站点编号为0到n-1。共有m辆公交车，每辆公交车的运行区间为a-b，表示公交车从a站点运行到b站点(a < b)，乘客可以在区间内的任意站点上下车进行换乘。小明需要从x站点乘坐公交到达v站点，请问至少需要乘坐几趟公交车?如果无法到达，则返回-1。如果起点和终点相同，则返回0。
输入描述
第一行输入为站点数n和公交数m，其中2<=n<=100，1<=m<=50第二行输入为小明的起点站x和终点站y，其中0<=x<=y<=n-1接下来m行为每趟公交车的起点站a和终点站b，其中0<=a<b<=n-1
输出描述
输出最小需乘坐的公交次数，如果无法到达，则返回-1。如果起点和终点相同，则返回 0。
补充说明：
m辆公交车的区间都不相同，但区间可能存在重叠。可将公交车视为单向运行，不用考虑往返 
示例1：
输入：
5 3
0 4
0 2
1 3
3 4
输出
3
说明
第一趟从站点0乘坐到站点2
第二趟从站点2乘坐到站点3
第三趟从站点3乘坐到站点4
最少需要乘坐3趟公交

示例2：
输入：
3 1
0 2
0 1
输出：
-1
说明：
无法达到

示例3：
输入：
4 4
1 1
0 1
1 2
2 3
0 3
输出：
0
说明：
小明从站点1到1不用车

思路：
bfs
一辆公交车的出发区间转化为，这一区间内所有点可以到达终点，建图。
```c++
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    while (cin >> n >> m)
    {
        int x, y;
        cin >> x >> y;
        vector<pair<int, int>> buses(m);
        for (auto &p : buses)
            cin >> p.first >> p.second;
        if (x == y)
        {
            cout << 0 << "\n";
            continue;
        }
        unordered_map<int, vector<int>> g;
        for (int i = 0; i < m; i++)
        {
            for (int j = buses[i].first; j <= buses[i].second; j++)
            {
                g[j].push_back(i);
            }
        }
        queue<int> q;
        vector<bool> vis1(n, false);
        vector<bool> vis2(m, false);
        q.push(x);
        vis1[x] = true;
        int res = 0;
        bool found = false;
        while (!q.empty())
        {
            int size = q.size();
            res++;
            for (int i = 0; i < size; i++)
            {
                int current = q.front();
                q.pop();
                for (auto bus : g[current])
                {
                    if (vis2[bus])
                        continue;
                    vis2[bus] = true;
                    for (int j = buses[bus].first; j <= buses[bus].second; j++)
                    {
                        if (j == y)
                        {
                            found = true;
                            break;
                        }
                        if (!vis1[j])
                        {
                            vis1[j] = true;
                            q.push(j);
                        }
                    }
                    if (found)
                        break;
                }
                if (found)
                    break;
            }
            if (found)
            {
                cout << res << "\n";
                break;
            }
        }
        if (!found)
            cout << -1 << "\n";
    }
}

```

# 3
在河的两岸从左到右分别有若干桥墩，每个桥墩都有型号，小易需要在两岸分别找到型号一样的桥墩，才可以搭建一座敲。每个桥墩只能属一座桥，且搭建出来的桥不能相交。请问小易最多在河上能搭建出多少座桥?

输入描述：
每组输入两行，表示河岸两边的桥墩以及型号，桥墩按照输入的顺序从左到右排列，以空格隔开，河岸一侧的的桥墩数量不超过500个，桥从左到右排列敦型号为正整数目型号不超过200

例如：
1 2 3
1 2 4 3
一侧有三个桥墩，从左到右的型号分别为1 2 3。
河岸另一侧表示河有四个桥墩，从左到右的型号分别为1 2 4 3 
示例1
输入：
1 2 3
1 2 4 3
输出
3

说明：
输入:表示河岸一侧有三个桥墩，从左到右的型号分别为1 2 3。
河岸另一侧有四个桥墩，从左到右的型号分别为1243输出:能搭建出 1-1 2-2 3-3，所以输出3

示例2：
输入：
1 2 3
1 3 2
输出
2

说明：
输入:表示河岸一侧有三个桥墩，从左到右的型号分别为1 2 3。
河岸另一侧有三个桥墩，从左到右的型号分别为1 3 2
输出：能搭建出 1-1 2-2 或者 1-1 3-3 输出2

思路：
转化为最长公共子序列，（LCS）

```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1;
        while ((line1 = br.readLine()) != null) {
            line1 = line1.trim();
            if (line1.isEmpty()) {
                continue;
            }
            String line2 = br.readLine();
            if (line2 == null) {
                break;
            }
            line2 = line2.trim();
            int[] seqA = parseLine(line1);
            int[] seqB = parseLine(line2);
            int lcsLength = computeLCS(seqA, seqB);
            System.out.println(lcsLength);
        }
    }

    private static int[] parseLine(String line) {
        if (line.isEmpty()) {
            return new int[0];
        }
        String[] tokens = line.split("\\s+");
        int[] seq = new int[tokens.length];
        for (int i = 0; i < tokens.length; i++) {
            seq[i] = Integer.parseInt(tokens[i]);
        }
        return seq;
    }

    private static int computeLCS(int[] A, int[] B) {
        int n = A.length;
        int m = B.length;
        int[] previous = new int[m + 1];
        int[] current = new int[m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (A[i - 1] == B[j - 1]) {
                    current[j] = previous[j - 1] + 1;
                } else {
                    current[j] = Math.max(previous[j], current[j - 1]);
                }
            }
            int[] temp = previous;
            previous = current;
            current = temp;
        }
        return previous[m];
    }
}


```


# 4
到年末了，公司要组织团建，其中一个活动需要将所有人分为3个组，各个组分配不同的任务，为了更有新鲜感，HR小婷想要平时工位挨在一起的同事不能分在一个组，例如小明的左右分别是小王和小红，前面是小张，后面是小李，则他们都不能和小明分在同一个组。公司的工位分布共有 row 排，每排有 cnt 个工位，每个工位均坐有同事，所有同事都必须参加活动，请帮小婷计算出共有多少种分组可能性。因为结果可能非常大，请返回对 10^9+7 取余的结果。
输入描述
第一行输入为两个数字，以空格分割，格式为:row cnt，
其中 1<=row<=5、1<=cnt<= 1000
输出描述
输出为不同的分组情况数，结果需要对 10^9+7 取余
补充说明
三个组的人数不需要相等，允许部分组内没有人
示例1：
输入
1 1
输出
3
说明：
有 A B C三组，只有1个人甲，共有[甲--，-甲-，--甲]三种情况

实力2：
输入：
1 2
输出：
6
有ABC三组，甲乙两个人，甲乙一定是挨在一起的，
因此有[甲乙-,甲-乙. 乙甲 -，乙-甲,-甲乙,-乙甲]六种情况

输入：
3 3
输出
246

思路：
动态规划+状态压缩

状态枚举：
每一列的分配状态由row个工位的组分配情况组成，每个工位有3种选择（组A、B、C）。
通过枚举所有可能的状态，并筛选出在同一列内相邻工位不属于同一组的有效状态。
兼容状态预处理：
预计算每个状态之间是否兼容（即相邻列的相同工位不分配到同一组），以便在动态规划时快速查找。
动态规划：
使用两个数组dp_prev和dp_curr分别表示前一列和当前列的状态分配方式数。
对于每一列，遍历所有有效状态，并根据兼容性累加方式数。
结果计算：
最终的结果是所有可能的最后一列状态的方式数之和，取模10^9+7。
```c++
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int row, cnt;
    cin >> row >> cnt;
    int total_states = pow(3, row);
    vector<int> vs;
    vector<vector<int>> sc;
    for (int s = 0; s < total_states; s++)
    {
        vector<int> colors(row);
        int tmp = s;
        bool valid = true;
        for (int i = 0; i < row; i++)
        {
            colors[i] = tmp % 3;
            tmp /= 3;
            if (i > 0 && colors[i] == colors[i - 1])
            {
                valid = false;
                break;
            }
        }
        if (valid)
        {
            vs.push_back(s);
            sc.emplace_back(colors);
        }
    }
    int n = vs.size();
    vector<vector<int>> compat(n, vector<int>());
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            bool ok = true;
            for (int k = 0; k < row; k++)
                if (sc[i][k] == sc[j][k])
                {
                    ok = false;
                    break;
                }
            if (ok)
                compat[i].push_back(j);
        }
    }
    vector<long long> dp_prev(n, 1);
    for (int c = 2; c <= cnt; c++)
    {
        vector<long long> dp_curr(n, 0);
        for (int i = 0; i < n; i++)
        {
            for (auto &j : compat[i])
            {
                dp_curr[j] = (dp_curr[j] + dp_prev[i]) % MOD;
            }
        }
        dp_prev = dp_curr;
    }
    long long res = 0;
    for (auto &x : dp_prev)
        res = (res + x) % MOD;
    if (cnt == 0)
    {
        res = 1;
    }
    cout << res;
}

```