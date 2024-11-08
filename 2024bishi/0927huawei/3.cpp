#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int x, y, danger;
    Node(int _x, int _y, int _danger) : x(_x), y(_y), danger(_danger) {}
};
struct Compare
{
    bool operator()(const Node &a, const Node &b)
    {
        return a.danger < b.danger; 
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int M, N;
    cin >> M >> N;
    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    vector<vector<int>> g(M, vector<int>(N));
    vector<vector<int>> d(M, vector<int>(N, -1));
    vector<pair<int, int>> inf;

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> g[i][j];
            if (g[i][j] == 2 || g[i][j] == 3)
            {
                d[i][j] = 0;
                inf.emplace_back(i, j);
            }
        }
    }

    int day = 0;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    while (!inf.empty())
    {
        day++;
        vector<vector<int>> D(M, vector<int>(N, 0));

        priority_queue<Node, vector<Node>, Compare> pq;

        for (auto &[x, y] : inf)
        {
            int danger = (g[x][y] == 2) ? a2 : a1;
            pq.emplace(x, y, danger);
            D[x][y] = danger;
        }

        while (!pq.empty())
        {
            Node current = pq.top();
            pq.pop();
            int x = current.x, y = current.y, danger = current.danger;

            for (int k = 0; k < 4; k++)
            {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (nx >= 0 && nx < M && ny >= 0 && ny < N && g[nx][ny] != 1)
                {
                    int nd = danger - 1;
                    if (nd > 0 && D[nx][ny] < nd)
                    {
                        D[nx][ny] = nd;
                        pq.emplace(nx, ny, nd);
                    }
                }
            }
        }

        vector<pair<int, int>> newInf;
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if ((g[i][j] == 4 || g[i][j] == 5) && d[i][j] == -1)
                {
                    int th = (g[i][j] == 4) ? b2 : b1;
                    if (D[i][j] >= th)
                    {
                        d[i][j] = day;
                        newInf.emplace_back(i, j);
                    }
                }
            }
        }

        for (auto &[x, y] : newInf)
        {
            if (g[x][y] == 4)
                g[x][y] = 2;
            else if (g[x][y] == 5)
                g[x][y] = 3;
        }
        inf = move(newInf);
    }

    for (int i = 0; i < M; i++)
    {
        string res_line;
        for (int j = 0; j < N; j++)
        {
            int res;
            if (g[i][j] == 0 || g[i][j] == 1)
            {
                res = -1;
            }
            else
            {
                res = d[i][j];
            }
            res_line += to_string(res);
            if (j != N - 1)
                res_line += ' ';
        }
        cout << res_line << '\n';
    }
}
