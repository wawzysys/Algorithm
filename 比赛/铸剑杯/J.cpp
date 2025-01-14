#include <bits/stdc++.h>
using namespace std;

struct Edge
{
    int to, rev;
    long long cap;
};

class MaxFlow
{
public:
    int n;
    vector<vector<Edge>> graph;
    vector<int> level;
    vector<int> ptr;

    MaxFlow(int size)
    {
        n = size;
        graph.resize(n + 1, vector<Edge>());
        level.resize(n + 1);
        ptr.resize(n + 1);
    }

    void add_edge(int from, int to, long long cap)
    {
        Edge a = {to, (int)graph[to].size(), cap};
        Edge b = {from, (int)(graph[from].size()), 0};
        graph[from].push_back(a);
        graph[to].push_back(b);
    }

    bool bfs(int s, int t)
    {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        q.push(s);
        level[s] = 0;
        while (!q.empty())
        {
            int u = q.front();
            q.pop();
            for (auto &e : graph[u])
            {
                if (e.cap > 0 && level[e.to] == -1)
                {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                    if (e.to == t)
                        return true;
                }
            }
        }
        return false;
    }

    long long dfs(int u, int t, long long flow)
    {
        if (u == t)
            return flow;
        for (int &i = ptr[u]; i < graph[u].size(); ++i)
        {
            Edge &e = graph[u][i];
            if (e.cap > 0 && level[e.to] == level[u] + 1)
            {
                long long pushed = dfs(e.to, t, min(flow, e.cap));
                if (pushed > 0)
                {
                    e.cap -= pushed;
                    graph[e.to][e.rev].cap += pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }

    long long max_flow(int s, int t)
    {
        long long flow = 0;
        while (bfs(s, t))
        {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, 1e18))
            {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    MaxFlow mf(n);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        mf.add_edge(a, b, c);
    }
    cout << mf.max_flow(1, n);
}
