#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll INF = LLONG_MAX;

// 定义最大积分和优惠券数量
const int MAX_POINTS = 100;
const int MAX_COUPONS = 4; // 根据情况调整

// 将dp数组定义为全局变量
ll dp[1001][MAX_POINTS][MAX_COUPONS][MAX_COUPONS][MAX_COUPONS];

ll solve(int n, vector<int> &P)
{
    // 初始化dp数组
    for (int day = 0; day <= n; ++day)
        for (int points = 0; points < MAX_POINTS; ++points)
            for (int c1 = 0; c1 < MAX_COUPONS; ++c1)
                for (int c2 = 0; c2 < MAX_COUPONS; ++c2)
                    for (int c3 = 0; c3 < MAX_COUPONS; ++c3)
                        dp[day][points][c1][c2][c3] = INF;

    dp[0][0][0][0][0] = 0;

    for (int day = 0; day < n; ++day)
    {
        for (int points = 0; points < MAX_POINTS; ++points)
        {
            for (int c1 = 0; c1 < MAX_COUPONS; ++c1)
            {
                for (int c2 = 0; c2 < MAX_COUPONS; ++c2)
                {
                    for (int c3 = 0; c3 < MAX_COUPONS; ++c3)
                    {
                        ll cost = dp[day][points][c1][c2][c3];
                        if (cost == INF)
                            continue;

                        // 优惠券状态转移
                        int new_c1 = c2; // c2的优惠券变为c1
                        int new_c2 = c3; // c3的优惠券变为c2
                        int new_c3 = 0;  // 新获得的优惠券将加入到c3

                        // 选项1：使用优惠券
                        if (new_c1 > 0)
                        {
                            int nc1 = new_c1 - 1;
                            int nc2 = new_c2;
                            int nc3 = new_c3;
                            dp[day + 1][points][nc1][nc2][nc3] = min(dp[day + 1][points][nc1][nc2][nc3], cost);
                        }

                        // 选项2：购买汉堡
                        int pi = P[day];
                        int np = points + pi;
                        int ncoupon = np / 100;
                        np %= 100;

                        int nc1 = new_c1;
                        int nc2 = new_c2;
                        int nc3 = new_c3 + ncoupon;
                        // 限制优惠券数量在范围内
                        if (nc3 >= MAX_COUPONS)
                            nc3 = MAX_COUPONS - 1;

                        dp[day + 1][np][nc1][nc2][nc3] = min(dp[day + 1][np][nc1][nc2][nc3], cost + pi);
                    }
                }
            }
        }
    }

    ll res = INF;
    for (int points = 0; points < MAX_POINTS; ++points)
    {
        for (int c1 = 0; c1 < MAX_COUPONS; ++c1)
        {
            for (int c2 = 0; c2 < MAX_COUPONS; ++c2)
            {
                for (int c3 = 0; c3 < MAX_COUPONS; ++c3)
                {
                    res = min(res, dp[n][points][c1][c2][c3]);
                }
            }
        }
    }
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        vector<int> P(n);
        for (int i = 0; i < n; ++i)
            cin >> P[i];
        ll ans = solve(n, P);
        cout << ans << "\n";
    }
    return 0;
}
