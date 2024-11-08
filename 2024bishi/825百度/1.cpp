#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n, x, y, k;
    cin >> n >> x >> y >> k;

    vector<int> a(n), b(n), c(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];
    for (int i = 0; i < n; i++)
        cin >> c[i];

    vector<vector<long long>> dp(n + 1, vector<long long>(3, 0));

    dp[0][0] = 0;
    dp[0][1] = 0;
    dp[0][2] = 0;

    for (int i = 1; i <= n; i++)
    {
        dp[i][0] = max(dp[i][0], dp[i - 1][0] + a[i - 1]); // Stay at top
        if (i >= x)
            dp[i][0] = max(dp[i][0], dp[i - x][1] + a[i - 1]); // Come from mid to top

        dp[i][1] = max(dp[i][1], dp[i - 1][1] + b[i - 1]); // Stay at mid
        if (i >= x)
            dp[i][1] = max(dp[i][1], dp[i - x][0] + b[i - 1]); // Come from top to mid
        if (i >= y)
            dp[i][1] = max(dp[i][1], dp[i - y][2] + b[i - 1]); // Come from bottom to mid

        dp[i][2] = max(dp[i][2], dp[i - 1][2] + c[i - 1]); // Stay at bottom
        if (i >= y)
            dp[i][2] = max(dp[i][2], dp[i - y][1] + c[i - 1]); // Come from mid to bottom
    }

    // Find the maximum coins that can be collected at the last second
    long long result = max({dp[n][0], dp[n][1], dp[n][2]});
    cout << result << endl;

    return 0;
}
