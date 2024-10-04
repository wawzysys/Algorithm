#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> items(n);
    for (auto &p : items)
        cin >> p.first >> p.second;

    sort(items.begin(), items.end(), [&](const pair<int, int> &a, const pair<int, int> &b) -> bool
         {
        if(a.first != b.first) return a.first > b.first;
        return a.second < b.second; });

    ll sum = 0;
    int cnt = 0;
    vector<int> freq(n + 1, 0);
    priority_queue<int, vector<int>, std::greater<int>> pq;
    for (int i = 0; i < k; ++i)
    {
        sum += items[i].first;
        if (++freq[items[i].second] == 1)
            cnt++;
        else
            pq.push(items[i].first);
    }

    vector<int> uniq;
    for (int i = k; i < n; ++i)
    {
        if (freq[items[i].second] == 0)
        {
            uniq.push_back(items[i].first);
        }
    }
    sort(uniq.begin(), uniq.end(), greater<int>());

    vector<ll> pre_pq, pre_uniq;
    ll s = 0;
    while (!pq.empty())
    {
        s += pq.top();
        pre_pq.push_back(s);
        pq.pop();
    }
    s = 0;
    for (auto p : uniq)
    {
        s += p;
        pre_uniq.push_back(s);
    }

    ll res = (ll)sum + (ll)cnt * cnt;
    int m = min((int)pre_pq.size(), (int)pre_uniq.size());
    for (int i = 1; i <= m; ++i)
    {
        ll tmp = sum - pre_pq[i - 1] + pre_uniq[i - 1] + (ll)(cnt + i) * (cnt + i);
        res = max(res, tmp);
    }
    cout << res;
}
