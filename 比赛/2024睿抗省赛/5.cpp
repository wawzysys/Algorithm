#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e5 + 5;
int fa[MAXN], sz[MAXN];
int dfn[MAXN], low[MAXN], clk = 0;
int n, m, edge_cnt[MAXN], ring_size = 0, ring_cnt = 0;
vector<int> g[MAXN];
bool vis[MAXN];

void init(int n)
{
    for (int i = 1; i <= n; i++)
    {
        fa[i] = i;
        sz[i] = 1;
        dfn[i] = low[i] = 0;
        edge_cnt[i] = 0;
        g[i].clear();
        vis[i] = false;
    }
}

int find(int x)
{
    return x == fa[x] ? x : fa[x] = find(fa[x]);
}

void merge(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx == fy)
        return;
    fa[fx] = fy;
    sz[fy] += sz[fx];
}

void tarjan(int u, int pre)
{
    dfn[u] = low[u] = ++clk;
    for (auto v : g[u])
    {
        if (!dfn[v])
        {
            tarjan(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] >= dfn[u] && pre != -1)
            {
                ring_size++;
            }
        }
        else if (v != pre)
        {
            low[u] = min(low[u], dfn[v]);
        }
    }
}

bool f()
{
    for (int i = 1; i <= n; i++)
    {
        if (edge_cnt[i] > 2)
        {
            ring_cnt++;
            ring_size = 0;
            for (auto v : g[i])
            {
                if (edge_cnt[v] > 1)
                {
                    tarjan(v, -1);
                }
            }
            if (ring_size == 1)
                ring_cnt--;
            if (ring_cnt > 1)
                return false;
        }
    }
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &n, &m);
        init(n);
        for (int i = 0; i < m; i++)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            g[u].push_back(v);
            g[v].push_back(u);
            edge_cnt[u]++;
            edge_cnt[v]++;
        }
        bool flag = f();
        if (flag && ring_cnt == 1)
        {
            printf("Yes %d\n", ring_size);
        }
        else
        {
            printf("No %d\n", ring_cnt);
        }
    }
    return 0;
}