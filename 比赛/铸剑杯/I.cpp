#include <bits/stdc++.h>
using namespace std;

struct RollbackDSU
{
    vector<int> parent;
    vector<int> size;
    int components;
    vector<pair<int, int>> history;

    RollbackDSU(int n_) : parent(n_ + 1), size(n_ + 1, 1), components(n_)
    {
        for (int i = 0; i <= n_; i++)
            parent[i] = i;
    }

    int find_set(int x)
    {
        while (x != parent[x])
            x = parent[x];
        return x;
    }

    void union_set(int x, int y)
    {
        int fx = find_set(x);
        int fy = find_set(y);
        if (fx == fy)
            return;
        if (size[fx] < size[fy])
            swap(fx, fy);
        history.emplace_back(fy, parent[fy]);
        history.emplace_back(-fx, size[fx]);
        parent[fy] = fx;
        size[fx] += size[fy];
        components--;
    }

    void rollback(int checkpoint)
    {
        while (history.size() > checkpoint)
        {
            auto [a, b] = history.back();
            history.pop_back();
            if (a < 0)
            {
                size[-a] = b;
            }
            else
            {
                parent[a] = b;
                components++;
            }
        }
    }
};

struct Edge
{
    int u, v;
};

struct SegmentTree
{
    int size;
    vector<vector<Edge>> tree;
    SegmentTree(int n_)
    {
        size = 1;
        while (size < n_)
            size <<= 1;
        tree.assign(2 * size, vector<Edge>());
    }
    void add_edge(int l, int r, Edge e, int node = 1, int nl = 0, int nr = -1)
    {
        if (nr == -1)
            nr = size;
        if (r <= nl || nr <= l)
            return;
        if (l <= nl && nr <= r)
        {
            tree[node].emplace_back(e);
            return;
        }
        int mid = (nl + nr) / 2;
        add_edge(l, r, e, 2 * node, nl, mid);
        add_edge(l, r, e, 2 * node + 1, mid, nr);
    }
    void traverse(int node, int nl, int nr, RollbackDSU &dsu, vector<int> &ans)
    {
        int checkpoint = dsu.history.size();
        for (auto &e : tree[node])
        {
            dsu.union_set(e.u, e.v);
        }
        if (nr - nl == 1)
        {
            ans[nl] = dsu.components;
        }
        else
        {
            int mid = (nl + nr) / 2;
            traverse(2 * node, nl, mid, dsu, ans);
            traverse(2 * node + 1, mid, nr, dsu, ans);
        }
        dsu.rollback(checkpoint);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, k;
    cin >> n >> m >> k;
    auto get_key = [&](int a, int b) -> long long
    {
        if (a > b)
            swap(a, b);
        return (long long)a * 100000 + b;
    };
    unordered_map<long long, vector<pair<int, int>>> edge_intervals;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        long long key = get_key(a, b);
        edge_intervals[key].emplace_back(0, k);
    }
    vector<tuple<int, int, int>> events(k);
    unordered_map<long long, int> last_add;
    for (int i = 0; i < k; i++)
    {
        int t, a, b;
        cin >> t >> a >> b;
        events[i] = make_tuple(t, a, b);
        long long key = get_key(a, b);
        if (t == 1)
        {
            last_add[key] = i + 1;
        }
        else
        {
            if (last_add.find(key) != last_add.end())
            {
                int start = last_add[key];
                edge_intervals[key].emplace_back(start, i);
                last_add.erase(key);
            }
            else
            {
                edge_intervals[key].emplace_back(0, i);
            }
        }
    }
    for (auto &[key, lst] : last_add)
    {
        edge_intervals[key].emplace_back(lst, k);
    }
    SegmentTree st(k + 1);
    for (auto &[key, intervals] : edge_intervals)
    {
        int u = key / 100000;
        int v = key % 100000;
        for (auto &[l, r] : intervals)
        {
            st.add_edge(l, r + 1, Edge{u, v});
        }
    }
    RollbackDSU dsu(n);
    vector<int> ans(k + 1, 0);
    st.traverse(1, 0, st.size, dsu, ans);
    for (int i = 0; i <= k; i++)
        cout << ans[i] << (i == k ? '\n' : ' ');
}
