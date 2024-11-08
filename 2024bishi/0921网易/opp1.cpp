#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &x : a)
        cin >> x;
    vector<int> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    unordered_map<int, int> m;
    for (auto x : a)
        m[x]++;
    unordered_map<int, int> cnt;
    ll ans = 0;
    for (int j = 0; j < n; j++)
    {
        int val = a[j];
        m[val]--;
        int x = val + 1;
        if (m.find(x) != m.end())
        {
            ll cb = cnt[x];
            ll cf = m[x];
            ans += cb * cf;
        }
        cnt[val]++;
    }
    cout << ans;
}
