#include <bits/stdc++.h>
using namespace std;

const int N = 1010;
const int M = 1000010;

int n, a[N];
bool use[M];
int b[N], idx;

int solve(int x)
{
    idx = 0;
    for (int i = 1; i <= n; i++)
        if (a[i] != x)
            b[++idx] = a[i];
    int res = 0;
    for (int l = 1, r = 1; l <= idx; r++, l = r)
    {
        while (r < idx && b[r + 1] == b[l])
            ++r;
        res = max(res, r - l + 1);
    }
    return res;
}

signed main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
        use[a[i]] = true;
    }
    int ans1 = 0;
    for (int l = 1, r = 1; l <= n; r++, l = r)
    {
        while (r < n && a[r + 1] == a[l])
            ++r;
        ans1 = max(ans1, r - l + 1);
    }
    int ans2 = 0;
    for (int i = 1; i <= M - 10; i++)
    {
        if (!use[i])
            continue;
        ans2 = max(ans2, solve(i));
    }
    printf("%lld\n", ans2 - ans1);
    return 0;
}