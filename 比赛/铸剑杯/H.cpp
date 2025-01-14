#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;
    while (t--)
    {
        ll y, x;
        cin >> y >> x;
        ll k = max(y, x);
        ll ans = 0;
        if (k % 2 == 0)
        {
            // Even layer
            if (y == k)
            {
                ans = k * k - x + 1;
            }
            else
            {
                ans = (k - 1) * (k - 1) + y;
            }
        }
        else
        {
            // Odd layer
            if (x == k)
            {
                ans = k * k - y + 1;
            }
            else
            {
                ans = (k - 1) * (k - 1) + x;
            }
        }
        cout << ans << "\n";
    }
}
