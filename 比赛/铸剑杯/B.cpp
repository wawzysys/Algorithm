#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    // 读取每个房间的硬币数量，1-based indexing
    vector<ll> k(n + 1, 0);
    for (int i = 1; i <= n; i++)
        cin >> k[i];

    // 构建有向图的邻接表
    vector<vector<int>> adj(n + 1, vector<int>());
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    // 初始化DP数组和状态数组
    // dp[u] = -1 表示未计算
    vector<ll> dp(n + 1, -1);
    // state[u] = 0: 未处理, 1: 正在处理, 2: 已处理
    vector<int> state(n + 1, 0);

    ll max_sum = 0;

    // 使用显式栈进行迭代DFS
    // 每个栈元素是一个 pair，其中first是节点编号，second是是否已处理完子节点
    vector<pair<int, bool>> stack;

    for (int u = 1; u <= n; u++)
    {
        if (dp[u] == -1)
        {
            stack.emplace_back(u, false);
            while (!stack.empty())
            {
                auto [current, processed] = stack.back();
                stack.pop_back();

                if (processed)
                {
                    // 计算 dp[current] = k[current] + max(dp[v] for v ∈ 出边(current))
                    ll current_sum = k[current];
                    for (auto &v : adj[current])
                    {
                        if (state[v] == 2)
                        {
                            current_sum = max(current_sum, k[current] + dp[v]);
                        }
                    }
                    dp[current] = current_sum;
                    state[current] = 2;
                    max_sum = max(max_sum, dp[current]);
                }
                else
                {
                    if (state[current] == 1)
                    {
                        // 检测到环，当前节点只能取自身的硬币
                        dp[current] = k[current];
                        state[current] = 2;
                        max_sum = max(max_sum, dp[current]);
                        continue;
                    }
                    state[current] = 1;
                    stack.emplace_back(current, true);
                    // 遍历所有出边的邻居
                    for (auto &v : adj[current])
                    {
                        if (dp[v] == -1 && state[v] == 0)
                        {
                            stack.emplace_back(v, false);
                        }
                    }
                }
            }
        }
    }

    cout << max_sum;
}
