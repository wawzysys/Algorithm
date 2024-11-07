#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int m, n, a1, a2, b1, b2, k;
    cin >> m >> n >> a1 >> a2 >> b1 >> b2 >> k;
    vector<vector<bool>> blk(m, vector<bool>(n, false));
    for (int i = 0; i < k; i++)
    {
        int x, y;
        cin >> x >> y;
        blk[x][y] = 1;
    }
    if (a1 == b1 && a2 == b2)
    {
        cout << 0;
        return 0;
    }
    if (blk[a1][a2] || blk[b1][b2])
    {
        cout << -1;
        return 0;
    }
    vector<vector<bool>> vis(m, vector<bool>(n, false));
    queue<tuple<int, int, int>> q;
    q.push({a1, a2, 0});
    vis[a1][a2] = 1;
    while (!q.empty())
    {
        auto [x, y, d] = q.front();
        q.pop();
        for (auto &[dx, dy] : vector<pair<int, int>>{make_pair(-1, 0), make_pair(1, 0), make_pair(0, -1), make_pair(0, 1)})
        {
            int nx = x + dx, ny = y + dy;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !vis[nx][ny] && !blk[nx][ny])
            {
                if (nx == b1 && ny == b2)
                {
                    cout << d + 1;
                    return 0;
                }
                vis[nx][ny] = 1;
                q.push({nx, ny, d + 1});
            }
        }
    }
    cout << -1;
}
