#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> S(n);
    for (auto &x : S)
        cin >> x;
    const int MAX = 131072;
    vector<int> d(MAX, -1);
    queue<int> q;
    q.push(0);
    d[0] = 0;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int i = 0; i < 17; i++)
        {
            int v = u ^ (1 << i);
            if (v < MAX && d[v] == -1)
            {
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
        for (auto s : S)
        {
            int v = u ^ s;
            if (v < MAX && d[v] == -1)
            {
                d[v] = d[u] + 1;
                q.push(v);
            }
        }
    }
    int Q;
    cin >> Q;
    while (Q--)
    {
        int a, b;
        cin >> a >> b;
        int c = a ^ b;
        cout << d[c] << "\n";
    }
}
