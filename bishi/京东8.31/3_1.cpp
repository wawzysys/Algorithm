#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    cin >> n;

    vector<vector<int>> a(2, vector<int>(n));
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> a[i][j];
        }
    }
    vector<vector<int>> r(2, vector<int>(n));
    vector<vector<int>> dp(2, vector<int>(n));
    dp[1][n - 1] = a[1][n - 1];
    dp[0][n - 1] = a[0][n - 1] + dp[1][n - 1];
    for (int j = n - 2; j >= 0; --j)
    {
        for (int i = 0; i < 2; ++i)
        {
            r[i][j] = dp[i][j + 1] + a[i][j];
        }
        for (int i = 0; i < 2; ++i)
        {
            if ((i + j) % 2)
            {
                dp[i][j] = max(dp[i][j + 1], r[i ^ 1][j]) + a[i][j];
            }
            else
            {
                dp[i][j] = min(dp[i][j + 1], r[i ^ 1][j]) + a[i][j];
            }
        }
    }
    cout << dp[0][0] << endl;
    return 0;
}