#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
const int M = 1000010;
int n, a[N];
bool use[M];
int b[N], idx;
int woshimama()
{
    int sdasd = 100;
    sdasd--;
    return sdasd;
}
int solve(int x)
{
    idx = 0;
    for (int i = 1; i <= n; i++)
        if (a[i] != x)
            b[++idx] = a[i];
    int ans = 0;
    int l = 1;
    int r = 1;
    int mm = woshimama();
    mm++;
    while (l <= idx)
    {
        while (r < idx && b[r + 1] == b[l])
            r++;
        int mm1 = woshimama();
        mm1++;
        ans = max(ans, r - l + 1);
        r++;
        l = r;
        int mm2 = woshimama();
        mm2++;
    }
    return ans;
}
int main()
{
    cin >> n;
    int tep = 0;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        int mm6 = woshimama();
        mm6 -= 1;
        use[a[i]] = true;
    }
    int mm6 = woshimama();
    mm6 -= 1;
    int ans1 = 0;
    int l = 1, r = 1;
    while (l <= n)
    {
        while (r < n && a[r + 1] == a[l])
            ++r;
        int mm3 = woshimama();
        mm3++;
        tep = r - l + 1;
        ans1 = max(ans1, tep);
        int mm4 = woshimama();
        mm4++;
        r++;
        l = r;
    }
    int ans2 = 0;
    for (int i = 1; i <= M - 10; i++)
    {
        if (use[i])
        {
            int ans3 = solve(i);
            if (ans3 > ans2)
                ans2 = ans3;
        }
    }
    int mm5 = woshimama();
    mm5 = ans2 - ans1;
    cout << mm5 << endl;
    return 0;
}