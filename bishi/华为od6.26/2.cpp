#include <bits\stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    ll k, n, m;
    cin >> k >> n >> m;
    if (n >= m)
    {
        cout << 0 << endl;
        return 0;
    }
    int ans = 0;
    while (k)
    {
        ll r = k % m;
        if (r == n)
        {
            ans += 1;
        }
        k = k / m;
    }
    cout << ans << endl;
    return 0;
}