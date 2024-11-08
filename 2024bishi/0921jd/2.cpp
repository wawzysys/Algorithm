#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<pair<ll, ll>> cars(n);
    for (int i = 0; i < n; i++)
        cin >> cars[i].first >> cars[i].second;

    sort(cars.begin(), cars.end(), [&](const pair<ll, ll> &a, const pair<ll, ll> &b) -> bool
         { return a.first < b.first; });

    vector<ll> speeds(n);
    for (int i = 0; i < n; i++)
        speeds[i] = cars[i].second;

    vector<ll> dp;
    for (auto &v : speeds)
    {

        auto it = upper_bound(dp.begin(), dp.end(), v);
        if (it == dp.end())
            dp.push_back(v);
        else
            *it = v;
    }

    ll L = dp.size();
    cout << (n - L);
}
