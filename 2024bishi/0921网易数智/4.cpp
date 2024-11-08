#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int row, cnt;
    cin >> row >> cnt;
    int total_states = pow(3, row);
    vector<int> vs;
    vector<vector<int>> sc;
    for (int s = 0; s < total_states; s++)
    {
        vector<int> colors(row);
        int tmp = s;
        bool valid = true;
        for (int i = 0; i < row; i++)
        {
            colors[i] = tmp % 3;
            tmp /= 3;
            if (i > 0 && colors[i] == colors[i - 1])
            {
                valid = false;
                break;
            }
        }
        if (valid)
        {
            vs.push_back(s);
            sc.emplace_back(colors);
        }
    }
    int n = vs.size();
    vector<vector<int>> compat(n, vector<int>());
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            bool ok = true;
            for (int k = 0; k < row; k++)
                if (sc[i][k] == sc[j][k])
                {
                    ok = false;
                    break;
                }
            if (ok)
                compat[i].push_back(j);
        }
    }
    vector<long long> dp_prev(n, 1);
    for (int c = 2; c <= cnt; c++)
    {
        vector<long long> dp_curr(n, 0);
        for (int i = 0; i < n; i++)
        {
            for (auto &j : compat[i])
            {
                dp_curr[j] = (dp_curr[j] + dp_prev[i]) % MOD;
            }
        }
        dp_prev = dp_curr;
    }
    long long res = 0;
    for (auto &x : dp_prev)
        res = (res + x) % MOD;
    if (cnt == 0)
    {
        res = 1;
    }
    cout << res;
}
