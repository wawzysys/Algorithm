#include <bits/stdc++.h>
using namespace std;

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    int n;
    cin >> n;
    vector<int> d(n + 1, 0);
    for (int i = 0; i < n - 1; ++i)
    {
        int u, v;
        cin >> u >> v;
        d[u] += 1;
        d[v] += 1;
    }
    int ans = 0;
    for (int deg : d)
    {
        if (deg >= 2)
        {
            ans += deg * (deg - 1) / 2;
        }
    }
    cout << ans << endl;

    return 0;
}
