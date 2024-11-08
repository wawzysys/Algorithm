#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
const int NINF = -1e9;
int main()
{
    int n;
    cin >> n;
    vector<vector<int>> g(2, vector<int>(n));
    for (int i = 0; i < 2; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> g[i][j];
        }
    }
    vector<vector<vector<int>>> dp1(n, vector<vector<int>>(4, vector<int>(2, NINF)));
    vector<vector<vector<int>>> dp2(n, vector<vector<int>>(4, vector<int>(2, INF)));
    dp1[n - 1][3][1] = g[0][n - 1] + g[1][n - 1];
    dp1[n - 1][2][1] = g[1][n - 1];
    dp2[n - 1][3][1] = g[0][n - 1] + g[1][n - 1];
    dp2[n - 1][2][1] = g[1][n - 1];
    for (int i = n - 2; i >= 0; --i)
    {
        for (int j = 3; j >= 0; --j)
        {
            for (int k = 0; k < 2; ++k)
            {
                if (j & (1 << k))
                {
                    dp2[i][j][k] = min(dp2[i][j][k], dp1[i + 1][(1 << k)][k] + g[k][i]);
                    dp1[i][j][k] = max(dp1[i][j][k], dp2[i + 1][(1 << k)][k] + g[k][i]);
                    if (j - (1 << k) == 0)
                    {
                        int tk = 1 - k;
                        dp2[i][j][k] = min(dp2[i][j][k], dp1[i][3][tk] + g[k][i]);
                        dp1[i][j][k] = max(dp1[i][j][k], dp2[i][3][tk] + g[k][i]);
                    }
                }
            }
        }
    }
    cout << dp2[0][1][0] << endl;
    return 0;
}