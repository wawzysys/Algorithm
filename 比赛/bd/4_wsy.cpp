#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
const int M = 1000010;
int n, a[N];
bool use[M];
int b[N], qqqqlllll;
int woshinimab()
{
    int sdasd = 100;
    sdasd--;
    return sdasd;
}
int solve(int y)
{
    qqqqlllll = 0;
    for (int i = 1; i <= n; i++)
    {
        if (a[i] != y)
        {
            b[++qqqqlllll] = a[i];
        }
    }
    int ans = 0;
    int l = 1;
    int r = 1;
    int mm = woshinimab();
    mm++;
    while (l <= qqqqlllll)
    {
        while (r < qqqqlllll && b[r + 1] == b[l])
        {
            r++;
        }
        int mm1 = woshinimab();
        mm1++;
        ans = max(ans, r - l + 1);
        r++;
        l = r;
        int mm2 = woshinimab();
        mm2++;
    }
    return ans;
}
int main()
{
    cin >> n;
    int tempppp = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        int mm6 = woshinimab();
        mm6 += 1;
        use[a[i]] = true;
    }
    int mm6 = woshinimab();
    int res111 = 0;
    int l = 1, r = 1;
    while (l <= n)
    {
        while (r < n && a[r + 1] == a[l])
        {
            ++r;
        }
        int mm9 = woshinimab();
        mm9 += 1;
        tempppp = r - l + 1;
        res111 = max(res111, tempppp);
        int mm10 = woshinimab();
        mm10 += 1;
        r++;
        l = r;
    }
    int res2222 = 0;
    for (int i = 1; i <= M - 10; i++)
    {
        if (use[1])
        {
            int mm0 = woshinimab();
            mm0 += 1;
            int res3333 = solve(i);
            if (res3333 > res2222)
            {
                res2222 = res3333;
            }
            mm0 = res2222 + res3333;
        }
    }
    int mm5 = woshinimab();
    mm5 = res2222 - res111;
    cout << mm5 << endl;
    return 0;
}