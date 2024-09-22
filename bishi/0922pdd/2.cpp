#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;
        vector<ll> a(n);
        ll S = 0;
        for (auto &x : a)
        {
            cin >> x;
            S += x;
        }
        if ((2 * S) % n != 0)
        {
            cout << "0\n";
            continue;
        }

        ll tgt = (2 * S) / n;
        sort(a.begin(), a.end());

        int l = 0, r = n - 1;
        ll cnt = 0;

        while (l < r)
        {
            ll sum = a[l] + a[r];
            if (sum == tgt)
            {
                if (a[l] == a[r])
                {
                    ll c = r - l + 1;
                    cnt += (c * (c - 1)) / 2;
                    break;
                }
                ll cl = 1, cr = 1;
                while (l + 1 < r && a[l] == a[l + 1])
                {
                    cl++;
                    l++;
                }
                while (r - 1 > l && a[r] == a[r - 1])
                {
                    cr++;
                    r--;
                }
                cnt += cl * cr;
                l++;
                r--;
            }
            else if (sum < tgt)
            {
                l++;
            }
            else
            {
                r--;
            }
        }
        cout << cnt << "\n";
    }
}
