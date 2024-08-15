#include <bits/stdc++.h>
using namespace std;
const int N = 1010;
char pre_grid[N][N];
char per_cold[N][N];
int n, m;
int er_x, er_y;
bool check(int x, int y)
{
    if (per_cold[x][y] != '.')
    {
        return false;
    }
    for (int i = max(0, x - 1); i < min(n, x + 2); i++)
    {
        for (int j = max(0, y - 1); j < min(m, y + 2); j++)
        {
            if (per_cold[i][j] == 'c' and (i != er_x or j != er_y))
            {
                return false;
            }
        }
    }
    return true;
}
int main()
{

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> pre_grid[i];
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            per_cold[i][j] = pre_grid[i][j];
            if (per_cold[i][j] == 'w')
            {
                per_cold[i][j] = 'c';
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (per_cold[i][j] == 'm')
            {
                for (int x = max(0, i - 1); x < min(n, i + 2); x++)
                {
                    for (int y = max(0, j - 1); y < min(m, j + 2); y++)
                    {
                        if (per_cold[x][y] == 'c')
                        {
                            per_cold[x][y] = 'w';
                        }
                    }
                }
            }
        }
    }
    er_x = -1;
    er_y = -1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (pre_grid[i][j] != per_cold[i][j])
            {
                er_x = i;
                er_y = j;
                break;
            }
        }
    }
    if (er_x == -1)
    {
        cout << "Too cold!" << endl;
        return 0;
    }
    vector<pair<int, int>> ans;
    for (int i = max(er_x - 1, 0); i < min(er_x + 2, n); i++)
    {
        for (int j = max(er_y - 1, 0); j < min(er_y + 2, m); j++)
        {
            if (check(i, j))
            {
                ans.push_back(make_pair(i, j));
            }
        }
    }
    if (ans.size() == 0)
    {
        cout << "Too cold!" << endl;
        return 0;
    }
    sort(ans.begin(), ans.end());
    for (auto c : ans)
    {
        cout << c.first + 1 << " " << c.second + 1 << endl;
    }
    return 0;
}