#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAX = 200005;

int in_time[MAX];
int out_time[MAX];
int timer_counter = 0;

vector<vector<int>> adj(MAX);

vector<int> flattened;
struct Query
{
    int L, R, idx;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> colors(n);
    for (auto &c : colors)
    {
        cin >> c;
    }

    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<int> sorted_colors = colors;
    sort(sorted_colors.begin(), sorted_colors.end());
    sorted_colors.erase(unique(sorted_colors.begin(), sorted_colors.end()), sorted_colors.end());

    auto get_compressed = [&](int x) -> int
    {
        return lower_bound(sorted_colors.begin(), sorted_colors.end(), x) - sorted_colors.begin() + 1;
    };
    flattened.resize(n + 1);
    function<void(int, int)> dfs = [&](int node, int parent)
    {
        in_time[node] = timer_counter;
        flattened[timer_counter] = get_compressed(colors[node - 1]);
        timer_counter++;
        for (auto &child : adj[node])
        {
            if (child != parent)
            {
                dfs(child, node);
            }
        }
        out_time[node] = timer_counter - 1;
    };

    flattened.assign(n, 0);
    dfs(1, -1);

    vector<Query> queries(n);
    for (int node = 1; node <= n; node++)
    {
        queries[node - 1].L = in_time[node];
        queries[node - 1].R = out_time[node];
        queries[node - 1].idx = node - 1;
    }

    int block_size = sqrt(n) + 1;

    sort(queries.begin(), queries.end(), [&](const Query &a, const Query &b) -> bool
         {
        if(a.L / block_size != b.L / block_size)
            return a.L / block_size < b.L / block_size;
        return (a.L / block_size &1) ? (a.R < b.R) : (a.R > b.R); });

    vector<int> freq(n + 2, 0);
    int unique_count = 0;

    vector<int> ans(n, 0);

    int curr_L = 0, curr_R = -1;

    for (auto &q : queries)
    {
        int L = q.L;
        int R = q.R;

        while (curr_L > L)
        {
            curr_L--;
            int color = flattened[curr_L];
            freq[color]++;
            if (freq[color] == 1)
            {
                unique_count++;
            }
        }
        while (curr_R < R)
        {
            curr_R++;
            int color = flattened[curr_R];
            freq[color]++;
            if (freq[color] == 1)
            {
                unique_count++;
            }
        }
        while (curr_L < L)
        {
            int color = flattened[curr_L];
            freq[color]--;
            if (freq[color] == 0)
            {
                unique_count--;
            }
            curr_L++;
        }
        while (curr_R > R)
        {
            int color = flattened[curr_R];
            freq[color]--;
            if (freq[color] == 0)
            {
                unique_count--;
            }
            curr_R--;
        }
        ans[q.idx] = unique_count;
    }
    for (int i = 0; i < n; i++)
    {
        cout << ans[i] << (i < n - 1 ? ' ' : '\n');
    }
}
