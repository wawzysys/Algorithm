#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N, M, K;
    cin >> N >> M >> K;
    unordered_map<int, vector<int>> adj;
    for (int i = 0; i < N; ++i)
    {
        int X, Y;
        cin >> X >> Y;
        adj[X].push_back(Y);
        adj[Y].push_back(X);
    }

    set<int> vis;
    queue<pair<int, int>> q;
    vis.insert(M);
    q.push({M, 0});

    while (!q.empty())
    {
        int node = q.front().first;
        int depth = q.front().second;
        q.pop();

        if (depth >= K)
            continue;

        for (int ne : adj[node])
        {
            if (vis.find(ne) == vis.end())
            {
                vis.insert(ne);
                q.push({ne, depth + 1});
            }
        }
    }

    cout << vis.size() - 1 << endl;
    return 0;
}
