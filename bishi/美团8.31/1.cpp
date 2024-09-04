#include <bits/stdc++.h>
using namespace std;
#define int long long
bool check(int mid, const vector<int> &positions, int k)
{
    vector<pair<int, int>> a;
    for (int pos : positions)
    {
        a.push_back({pos, pos + mid - 1});
    }
    vector<pair<int, int>> b;
    for (const auto &idx : a)
    {
        if (b.empty() || b.back().second < idx.first - 1)
        {
            b.push_back(idx);
        }
        else
        {
            b.back().second = max(b.back().second, idx.second);
        }
    }
    int total = 0;
    for (const auto &idx : b)
    {
        total += idx.second - idx.first + 1;
        if (total >= k)
            return true;
    }
    return total >= k;
}
int solve(int n, int k, vector<int> positions)
{
    sort(positions.begin(), positions.end());
    int low = 1, high = k;
    while (low < high)
    {
        int mid = low + (high - low) / 2;
        if (check(mid, positions, k))
        {
            high = mid;
        }
        else
        {
            low = mid + 1;
        }
    }
    return low;
}
signed main()
{
    int n, k;
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    cin >> n >> k;
    vector<int> positions(n);
    for (int i = 0; i < n; i++)
    {
        cin >> positions[i];
    }
    sort(positions.begin(), positions.end());
    cout << solve(n, k, positions) << endl;
    return 0;
}
