#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
using ll = long long;

int directions[] = {-1, 0, 1, 0, -1};

void solve()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    vector<vector<string>> grid(rows, vector<string>(cols));
    vector<vector<int>> diss(rows, vector<int>(cols, INF));
    vector<vector<int>> dE(rows, vector<int>(cols, INF));
    vector<vector<int>> weights(rows, vector<int>(cols, 0));

    priority_queue<pair<int, int>> startPQ, endPQ;

    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            char buffer[10];
            scanf("%s", buffer);
            grid[i][j] = string(buffer);
            if (grid[i][j] == "S")
            {
                diss[i][j] = 0;
                startPQ.push({0, i * cols + j});
            }
            else if (grid[i][j] == "E")
            {
                dE[i][j] = 0;
                endPQ.push({0, i * cols + j});
            }
            else if (grid[i][j] != "C" && grid[i][j] != "B")
            {
                weights[i][j] = stoi(grid[i][j]);
            }
        }
    }

    auto isValid = [&](int x, int y) -> bool
    {
        return weights[x][y] || !(grid[x][y] == "B");
    };

    auto u = [&](vector<vector<int>> &d, priority_queue<pair<int, int>> &pq)
    {
        while (!pq.empty())
        {
            auto current = pq.top();
            pq.pop();

            int distance = current.first, x = current.second / cols, y = current.second % cols;
            for (int k = 0; k < 4; ++k)
            {
                int newX = x + directions[k], newY = y + directions[k + 1];
                if (0 <= newX && newX < rows && 0 <= newY && newY < cols && isValid(newX, newY))
                {
                    if (weights[newX][newY])
                    {
                        int weight = weights[newX][newY];
                        if (d[newX][newY] > d[x][y] + weight)
                        {
                            d[newX][newY] = d[x][y] + weight;
                            pq.push({-d[newX][newY], newX * cols + newY});
                        }
                    }
                    else
                    {
                        if (d[newX][newY] > d[x][y])
                        {
                            d[newX][newY] = d[x][y];
                            pq.push({-d[newX][newY], newX * cols + newY});
                        }
                    }
                }
            }
        }
    };

    u(diss, startPQ);
    u(dE, endPQ);

    int minDistance = INF;
    for (int i = 0; i < rows; ++i)
    {
        for (int j = 0; j < cols; ++j)
        {
            if (grid[i][j] == "C" && diss[i][j] != INF && dE[i][j] != INF)
            {
                minDistance = min(minDistance, diss[i][j] + dE[i][j]);
            }
        }
    }

    if (minDistance == INF)
    {
        minDistance = -1;
    }
    printf("%d\n", minDistance);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    solve();

    return 0;
}
