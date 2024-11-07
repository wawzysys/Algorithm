#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}
int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i)
    {
        std::cin >> a[i];
    }
    std::vector<std::vector<int>> g(n + 1, std::vector<int>(n + 1));
    for (int i = 1; i <= n; i++)
    {
        g[i][i] = a[i];
        for (int j = i + 1; j <= n; ++j)
        {
            g[i][j] = gcd(g[i][j - 1], a[j]);
        }
    }
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, INT_MIN));
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int k = 1; k <= m; k++)
        {
            for (int j = k - 1; j < i; j++)
            {
                if (dp[j][k - 1] != INT_MIN)
                {
                    dp[i][k] = std::max(dp[i][k], dp[j][k - 1] + g[j + 1][i]);
                }
            }
        }
    }
    std::cout << dp[n][m] << std::endl;
    return 0;
}