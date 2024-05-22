#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;

int dirs[] = {-1, 0, 1, 0, -1};

void solve()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<std::string>> s(n, std::vector<std::string>(m));
    std::vector<std::vector<int>> f(n, std::vector<int>(m, inf));
    std::vector<std::vector<int>> g(n, std::vector<int>(m, inf));
    std::vector<std::vector<int>> digit(n, std::vector<int>(m, 0));

    std::priority_queue<std::pair<int, int>> pq1, pq2;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            std::cin >> s[i][j];
            if (s[i][j] == "S")
            {
                f[i][j] = 0;
                pq1.push({0, i * m + j});
            }
            else if (s[i][j] == "E")
            {
                g[i][j] = 0;
                pq2.push({0, i * m + j});
            }
            else if (s[i][j] != "C" and s[i][j] != "B")
            {
                digit[i][j] = stoi(s[i][j]);
            }
        }
    }
    auto check = [&](int i, int j) -> bool
    {
        return digit[i][j] or !(s[i][j] == "B");
    };
    auto update = [&](std::vector<std::vector<int>> &dp, std::priority_queue<std::pair<int, int>> &pq) -> void
    {
        while (!pq.empty())
        {
            auto t = pq.top();
            pq.pop();

            int d = t.first, x = t.second / m, y = t.second % m;
            for (int k = 0; k < 4; ++k)
            {
                int nx = x + dirs[k], ny = y + dirs[k + 1];
                if (0 <= nx and nx < n and 0 <= ny and ny < m and check(nx, ny))
                {
                    if (digit[nx][ny])
                    {
                        int w = digit[nx][ny];
                        if (dp[nx][ny] > dp[x][y] + w)
                        {
                            dp[nx][ny] = dp[x][y] + w;
                            pq.push({-dp[nx][ny], nx * m + ny});
                        }
                    }
                    else
                    {
                        if (dp[nx][ny] > dp[x][y])
                        {
                            dp[nx][ny] = dp[x][y];
                            pq.push({-dp[nx][ny], nx * m + ny});
                        }
                    }
                }
            }
        }
    };
    update(f, pq1);
    update(g, pq2);
    int ans = inf;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            if (s[i][j] == "C" and f[i][j] != inf and g[i][j] != inf)
            {
                ans = std::min(ans, f[i][j] + g[i][j]);
            }
        }
    }
    if (ans == inf)
        ans = -1;
    std::cout << ans << "\n";
}

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);

    solve();

    return 0;
}
