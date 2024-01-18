#include<bits/stdc++.h>
using namespace std;
#define int long long
int n;
int a[100005];
vector<int> grape[100005];
int dp[100005][2];
const int mod = 1e9 + 7;
int qp(int k, int w)
{
    int cnt = 1;
    while (w)
    {
        if (w % 2)
        {
            cnt *= k;
            cnt %= mod;
        }
        k *= k;
        k %= mod;
        w /= 2;
    }
    return cnt;
}
void dfs(int k, int fa)
{
    int sum = 1;
    if (k != 1 && grape[k].size() == 1)
    {
        if (a[k])
            dp[k][1] = 1;
        else dp[k][0] = 1;
        return;
    }
    for (int i = 0;i < grape[k].size();i++)
    {   int j = grape[k][i];
        if (j == fa)
            continue;
        dfs(j, k);
        sum *= (dp[j][1] + dp[j][0]) % mod;
        sum %= mod;
    }
    if (a[k] == 0) {
        dp[k][0] = sum;
        cout << k << "sum" << sum << endl;

        for (int i = 0;i < grape[k].size();i++)
        {   
            int j = grape[k][i];
            if (j == fa)
                continue;
            int temp1 = qp(((dp[j][1] + dp[j][0]) % mod), mod - 2) % mod ;
            int temp = sum * temp1 % mod;
            cout << k << "sum" << sum << "temp:" <<temp<< "j" << j <<"temp1:" << temp1 <<endl;
            dp[k][1] += temp * dp[j][1] % mod;
            dp[k][1] %= mod;
        }
    }else{
        dp[k][0] = 0;
        dp[k][1] = sum;

    }
}
signed main()
{
    cin >> n;
    int sum = 0;
    for (int i = 1;i <= n;i++)
    {
        scanf("%lld", &a[i]);
        sum += a[i];
    }
    // 没有红色
    if (sum == 0)
    {
        cout << 0 << endl;
        return 0;
    }
    // 就一个
    if (n == 1 && a[1] == 1){
        cout << 1 << endl;
        return 0;
    }
    if (n == 1&& a[1] == 0){
        cout << 0 << endl;
        return 0;
    }
    int l, r;
    for (int i = 1;i < n;i++)
    {
        scanf("%lld %lld", &l, &r);
        grape[l].push_back(r);
        grape[r].push_back(l);
    }
    dfs(1, 0);
    int ans = dp[1][1];
    for(int i = 1; i <= n ;i ++ ){
        cout << "i" << i << " "<<dp[i][0] << " " << dp[i][1] << endl;
    }
    printf("%lld", ans % mod);

    return 0;
}