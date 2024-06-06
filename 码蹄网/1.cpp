#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
typedef long long ll;
int n, m;
ll day[N], d[N], s[N], t[N], sub[N];
bool check(int x)
{
    memset(sub, 0, sizeof sub);
    for (int i = 1; i <= x; i++)
    {
        sub[s[i]] += d[i];
        sub[t[i] + 1] -= d[i];
    }
    for (int i = 1; i <= n; i++)
    {
        sub[i] += sub[i - 1];
        if (sub[i] > day[i])
            return true;
    }
    return false;
}
int main()
{
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        cin >> day[i];
    for (int i = 1; i <= m; i++)
        cin >> d[i] >> s[i] >> t[i];
    if (!check(m))
        cout << "0" << endl;
    else
    {
        cout << "-1" << endl;
        int l = 1, r = m;
        while (l <= r)
        {
            int mid = l + r >> 1;
            if (check(mid))
                r = mid - 1;
            else
                l = mid + 1;
        }
        cout << l << endl;
    }
}
