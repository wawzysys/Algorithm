#include<bits/stdc++.h>
using namespace std;
#define int long long
int T;
int n;
int a[100005];
int q[100005], f[100005];
int pr[200005];
signed main()
{
    for (int i = 2;i <= 200000;i++)
    {
        pr[i] = 1;
        for (int j = 2;j <= sqrt(i);j++)
        {
            if (i % j == 0)
            {
                pr[i] = 0;
                break;
            }
        }
    }
    scanf("%lld", &n);

    for (int i = 1;i <= n;i++)
    {
        scanf("%lld", &a[i]);
    }
    for (int i = 2;i <= n;i++)
    {
        q[i] = q[i - 1];
        if (pr[a[i] + a[i - 1]] != 1)q[i]++;
    }
    for (int i = n - 1;i >= 1;i--)
    {
        f[i] = f[i + 1];
        if (pr[a[i] + a[i + 1]] != 1)f[i]++;
    }
    for (int i = 0; i <= n; i ++ )
        cout << q[i] << " ";
        cout << endl;
    for (int i = 0; i <= n; i ++ )
        cout << f[i] << " ";
        cout << endl;
    int ans = -1;
    for (int i = 1;i < n;i++)
    {
        if (q[i - 1] || f[i + 2])continue;
        if (pr[a[i] + a[i + 1]] != 1)continue;
        if (i < n - 1 && pr[a[i] + a[i + 2]] != 1)continue;
        if (i > 1 && pr[(a[i + 1] + a[i - 1])] != 1)continue;
        if (ans != -1)
        {
            printf("-1\n");
            return 0;
        }
        ans = i;
    }
    printf("%lld\n", ans);
    return 0;
}