#include <bits/stdc++.h>
using namespace std;
const int maxn = 3005;
int arr[maxn][maxn];     // 输入的二维数组
bool vis[maxn][maxn][4]; // 记录每个位置的 4 个方向是否被访问过
bool mp[maxn][maxn];     // 记录每个位置是否被访问过

int main()
{
    int n, m;
    cin >> n >> m; // 输入矩阵的行列数

    // 输入矩阵
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }

    // 定义上下左右 4 个方向的偏移量
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    int x = 0, y = 0; // 初始位置
    int dir = 0;      // 初始方向为右
    int cnt = 0;      // 记录访问过的位置数

    // 模拟访问过程
    while (!vis[x][y][dir])
    {
        // 标记当前位置的当前方向已访问
        vis[x][y][dir] = true;

        // 如果当前位置未被访问过,则计数加 1
        if (!mp[x][y])
            cnt++, mp[x][y] = true;

        // 计算下一个位置的坐标
        int nxtX = x + dx[dir];
        int nxtY = y + dy[dir];

        // 如果下一个位置超出矩阵边界或者值为 1,则改变方向
        while (nxtX < 0 || nxtX >= n || nxtY < 0 || nxtY >= m || arr[nxtX][nxtY] == 1)
        {
            dir = (dir + 1) % 4; // 顺时针旋转方向
            nxtX = x + dx[dir];
            nxtY = y + dy[dir];
        }

        // 更新当前位置
        x = nxtX;
        y = nxtY;

        // 输出当前位置和方向
        cout << x << " " << y << " " << dir << endl;
    }

    // 输出访问过的位置数
    cout << cnt << endl;

    return 0;
}