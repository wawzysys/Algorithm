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
