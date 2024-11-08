#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    cin.ignore();
    vector<vector<int>> adj(n, vector<int>());
    for (int i = 0; i < n; ++i)
    {
        string line;
        getline(cin, line);
        if (!line.empty())
        {
            stringstream ss(line);
            int neighbor;
            while (ss >> neighbor)
            {
                adj[i].push_back(neighbor);
            }
            sort(adj[i].begin(), adj[i].end());
        }
    }
    vector<int> color(n, -1);
    bool possible = true;
    auto bfs = [&](int start) -> bool
    {
        queue<int> q;
        color[start] = 0;
        q.push(start);

        while (!q.empty())
        {
            int u = q.front();
            q.pop();

            for (int v : adj[u])
            {
                if (color[v] == -1)
                {
                    color[v] = 1 - color[u];
                    q.push(v);
                }
                else if (color[v] == color[u])
                {
                    return false;
                }
            }
        }
        return true;
    };
    for (int i = 0; i < n && possible; ++i)
    {
        if (color[i] == -1)
        {
            if (!bfs(i))
            {
                possible = false;
            }
        }
    }
    if (!possible)
    {
        cout << "-1\n";
    }
    else
    {
        vector<int> group0, group1;
        for (int i = 0; i < n; ++i)
        {
            if (color[i] == 0)
            {
                group0.push_back(i);
            }
            else
            {
                group1.push_back(i);
            }
        }
        sort(group0.begin(), group0.end());
        sort(group1.begin(), group1.end());
        auto printGroup = [&](const vector<int> &group)
        {
            if (group.empty())
            {
                cout << "\n";
                return;
            }
            for (size_t i = 0; i < group.size(); ++i)
            {
                if (i > 0)
                    cout << ' ';
                cout << group[i];
            }
            cout << '\n';
        };
        printGroup(group0);
        printGroup(group1);
    }

    return 0;
}
