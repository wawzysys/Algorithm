#include <bits/stdc++.h>
using namespace std;
int fa[222222];
int gf(int u)
{
    if (fa[u] == u)
    {
        return u;
    }
    return fa[u] = gf(fa[u]);
}
int a[222222];
int nt[222222];
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i)
    {
        scanf("%d", a + i);
    }
    for (int i = 1; i <= n; ++i)
    {
        fa[i] = i;
        // cout << i << " " << fa[i] << endl;
    }
    for (int i = n; i; --i)
    {
        int x = gf(a[i]);
        int y = fa[a[i]];
        nt[x] = i;
        fa[x] = i;
        cout << x << " " << y << " " << fa[x] << " " << nt[x] << endl;
    }
    for (int i = 1; i <= n; ++i)
    {
        cout << i << " " << nt[i] << endl;
    }
    int k = n;
    while (a[k] != 0)
        --k;
    while (k)
    {
        printf("%d ", k);
        k = nt[k];
    }
    return 0;
}
