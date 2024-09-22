#include <bits/stdc++.h>
using namespace std;

const int N = 2E5 + 10;
int n, a[N], f[N][30], lo[N];

void init()
{
    for (int j = 0; j <= 24; j++)
    {
        for (int i = 1; i + (1 << j) - 1 <= n; i++)
        {
            if (!j)
                f[i][j] = a[i];
            else
                f[i][j] = __gcd(f[i][j - 1], f[i + (1 << j - 1)][j - 1]);
        }
    }
}

int query(int l, int r)
{
    int k = lo[r - l + 1];
    return __gcd(f[l][k], f[r - (1 << k) + 1][k]);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    lo[1] = 0;
    for (int i = 2; i < N; i++)
    {
        lo[i] = lo[i / 2] + 1;
    }
    int T;
    cin >> T;
    while (T--)
    {
        cin >> n;
        for (int i = 1; i <= n; i++)
        {
            cin >> a[i];
        }
        init();
        int ans = 1 << 30;
        for (int i = 1; i <= n; i++)
        {
            int l = i, r = n;
            while (l < r)
            {
                int mid = l + r >> 1;
                if (query(i, mid) == 1)
                    r = mid;
                else
                    l = mid + 1;
            }
            if (query(i, r) == 1)
            {
                ans = min(ans, r - i + 1);
            }
        }
        if (ans == (1 << 30))
            ans = -1;
        cout << ans << '\n';
    }

    return 0;
}