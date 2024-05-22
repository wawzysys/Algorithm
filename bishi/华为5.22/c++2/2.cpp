#include <bits/stdc++.h>
using namespace std;
const int INF = numeric_limits<int>::max();
const vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
struct State
{
    int x, y, cost;
};

void bfs(const pair<int, int> &start, const vector<vector<string>> &grid, vector<vector<int>> &cost)
{
    int N = grid.size(), M = grid[0].size();
    queue<State> q;
    q.push({start.first, start.second, 0});
    cost[start.first][start.second] = 0;

    while (!q.empty())
    {
        auto [x, y, currentCost] = q.front();
        q.pop();

        for (auto [dx, dy] : directions)
        {
            int nx = x + dx;
            int ny = y + dy;
            if (nx < 0 || nx >= N || ny < 0 || ny >= M || grid[nx][ny] == "B")
            {
                continue;
            }
            int newCost = currentCost + (isdigit(grid[nx][ny][0]) ? stoi(grid[nx][ny]) : 0);
            if (newCost < cost[nx][ny])
            {
                cost[nx][ny] = newCost;
                q.push({nx, ny, newCost});
            }
        }
    }
}
int minn(int N, int M, vector<vector<string>> &grid)
{
    pair<int, int> start, end;
    vector<pair<int, int>> cg;
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (grid[i][j] == "S")
            {
                start = {i, j};
            }
            else if (grid[i][j] == "E")
            {
                end = {i, j};
            }
            else if (grid[i][j] == "C")
            {
                cg.push_back({i, j});
            }
        }
    }

    if (cg.empty())
    {
        return -1;
    }
    vector<vector<int>> sta(N, vector<int>(M, INF));
    bfs(start, grid, sta);
    vector<vector<int>> ce(N, vector<int>(M, INF));
    bfs(end, grid, ce);
    int mt = INF;
    for (auto &cp : cg)
    {
        if (sta[cp.first][cp.second] < INF && ce[cp.first][cp.second] < INF)
        {
            int totalCost = sta[cp.first][cp.second] + ce[cp.first][cp.second];
            mt = min(mt, totalCost);
        }
    }

    return mt == INF ? -1 : mt;
}

int main()
{
    int N, M;
    cin >> N >> M;
    vector<vector<string>> grid(N, vector<string>(M));
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            cin >> grid[i][j];
        }
    }

    int result = minn(N, M, grid);
    cout << result << endl;

    return 0;
}
