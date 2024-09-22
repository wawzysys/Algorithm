

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
void solve()
{
    int n;
    cin >> n;
    vector<int> p(n + 1);
    for (int i = 1; i <= n; i++)
        cin >> p[i];
    vector<int> vis(n + 1);
    int ok = 1;
    int str = -1;
    int xa, y;
    int idx = 0;
    int cnt = 0;
    function<int(int)> dfs = [&](int x)
    {
        cnt++;
        assert(cnt <= 1e6);
        if (vis[x])
            return x;
        xa = min(x, xa);
        y = max(y, x);
        idx++;
        vis[x] = 1;
        return dfs(p[x]);
    };

    for (int i = 1; i <= n; i++)
    {
        if (vis[i] == 0)
        {
            xa = 1e9;
            y = -1;
            str = i;
            int ed = dfs(i);
            if (str != ed)
            {
                ok = 0;
                break;
            }
            if (y - xa == idx - 1)
                continue;
            else
            {
                ok = 0;
                break;
            }
        }
        else
            continue;
    }
    cout << (ok ? 1 : -1) << endl;
}

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T = 1;
    cin >> T;
    while (T--)
        solve();
    return 0;
}
