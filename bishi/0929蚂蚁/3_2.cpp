#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        int total = n + m + 1;
        vector<pair<ll, ll>> v(total);
        ll sum_y = 0;
        for (auto &p : v)
        {
            cin >> p.first >> p.second;
            sum_y += p.second;
        }
        vector<pair<ll, int>> d(total);
        for (int i = 0; i < total; i++)
            d[i] = {v[i].first - v[i].second, i};
        sort(d.begin(), d.end(), [&](pair<ll, int> a, pair<ll, int> b) -> bool
             {
            if(a.first != b.first) return a.first > b.first;
            return a.second < b.second; });
        vector<ll> prefix(n + 1, 0);
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + d[i].first;
        vector<int> rank(total, 0);
        for (int i = 0; i < total; i++)
            rank[d[i].second] = i;
        ll top_n_sum = prefix[n];
        vector<ll> res(total, 0);
        for (int i = 0; i < total; i++)
        {
            if (rank[i] < n)
            {
                if (n < total)
                {
                    res[i] = sum_y + top_n_sum - (v[i].first - v[i].second) + d[n].first;
                }
                else
                {
                    res[i] = sum_y + top_n_sum - (v[i].first - v[i].second);
                }
            }
            else
            {
                res[i] = sum_y + top_n_sum;
            }
        }
        for (int i = 0; i < total; i++)
            cout << res[i] << (i < total - 1 ? " " : "\n");
    }
}
