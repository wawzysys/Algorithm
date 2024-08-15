#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 + 10;
int n;
int a[N], s[N], cc[2];
int b[N];

signed main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        if (a[i] == 1)
            a[i] = 1;
        if (a[i] == 0)
            a[i] = -1;
        s[i] = s[i - 1] + a[i];
    }

    int t = cc[0] - cc[1];

    int v = 0, vv = 0, kk = 0, k = 0;
    for (int i = 1; i <= n; i++)
    {
        kk = max(kk, s[i] - v);
        v = min(v, s[i]);
        k = min(k, s[i] - vv);
        vv = max(vv, s[i]);
    }

    int y = s[n] - k * 2, x = s[n] - kk * 2;
    int res;
    if (x >= 0)
        res = (x - y) / 2 + 1;
    else if (y <= 0)
        res = (x - y) / 2 + 1;
    else
    {
        int z = max(abs(x), abs(y));
        if (y % 2 == 1)
            res = (z + 1) / 2;
        else
            res = z / 2 + 1;
    }
    cout << res << '\n';
    return 0;
}

/*
0110 - 0
1110 - 2
0000 - 4

0 1 1 0
-2 2 2 -2

1 0 0 0  2
2 -2 -2 -2   4,0,2

*/