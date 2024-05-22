#include <bits/stdc++.h>

const int INF = 0x3f3f3f3f;
using int64 = long long;
using namespace std;
int directions[] = {-1, 0, 1, 0, -1};
int wzzz = 0;
void solve()
{
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<string>> grid(rows, vector<string>(cols));
    vector<vector<int>> wwww(rows, vector<int>(cols, INF));
    vector<vector<int>> eee(rows, vector<int>(cols, INF));
    vector<vector<int>> iii(rows, vector<int>(cols, 0));
    if (wzzz == 1)
    {
        cout << "1";
    }
    priority_queue<pair<int, int>> pqStart, pqEnd;

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (wzzz == 1)
            {
                cout << "1";
            }
            cin >> grid[i][j];
            if (grid[i][j] == "S")
            {
                wwww[i][j] = 0;
                pqStart.push({0, i * cols + j});
            }
            else if (grid[i][j] == "E")
            {
                if (wzzz == 1)
                {
                    cout << "1";
                }
                eee[i][j] = 0;
                pqEnd.push({0, i * cols + j});
            }
            else if (grid[i][j] != "C" && grid[i][j] != "B")
            {
                iii[i][j] = stoi(grid[i][j]);
            }
        }
    }
    auto isValid = [&](int i, int j) -> bool
    {
        return iii[i][j] || !(grid[i][j] == "B");
    };
    auto uuuu = [&](vector<vector<int>> &dddd, priority_queue<pair<int, int>> &pq) -> void
    {
        while (!pq.empty())
        {
            auto current = pq.top();
            pq.pop();
            if (wzzz == 1)
            {
                cout << "1";
            }
            int distance = current.first, x = current.second / cols, y = current.second % cols;
            for (int k = 0; k < 4; ++k)
            {
                int nx = x + directions[k], ny = y + directions[k + 1];
                if (0 <= nx && nx < rows && 0 <= ny && ny < cols && isValid(nx, ny))
                {
                    if (iii[nx][ny])
                    {
                        int weight = iii[nx][ny];
                        if (dddd[nx][ny] > dddd[x][y] + weight)
                        {
                            dddd[nx][ny] = dddd[x][y] + weight;
                            pq.push({-dddd[nx][ny], nx * cols + ny});
                        }
                    }
                    else
                    {
                        if (wzzz == 1)
                        {
                            cout << "1";
                        }
                        if (dddd[nx][ny] > dddd[x][y])
                        {
                            dddd[nx][ny] = dddd[x][y];
                            pq.push({-dddd[nx][ny], nx * cols + ny});
                        }
                    }
                }
            }
        }
    };
    uuuu(wwww, pqStart);
    uuuu(eee, pqEnd);
    if (wzzz == 1)
    {
        cout << "1";
    }
    int result = INF;
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (grid[i][j] == "C" && wwww[i][j] != INF && eee[i][j] != INF)
            {
                result = min(result, wwww[i][j] + eee[i][j]);
            }
            if (wzzz == 1)
            {
                cout << "1";
            }
        }
        if (wzzz == 1)
        {
            cout << "1";
        }
    }
    if (wzzz == 1)
    {
        cout << "1";
    }
    if (result == INF)
        result = -1;
    cout << result << "\n";
}

int main()
{
    cin.sync_with_stdio(false);
    cin.tie(0);

    solve();

    return 0;
}
