#include <iostream>
using namespace std;

const int N = 2020;   // 用于处理坐标范围的大小常数
int diff[N][N] = {0}; // 差分数组，用于记录影响范围的变化

// 插入操作，在给定矩形区域上添加影响值
void insert(int x1, int y1, int x2, int y2, int c)
{
    diff[x1][y1] += c;
    diff[x1][y2 + 1] -= c;
    diff[x2 + 1][y1] -= c;
    diff[x2 + 1][y2 + 1] += c;
}

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);

    int n, q;
    std::cin >> n;

    // 处理每个建筑物的信息，并在差分数组中记录影响范围
    for (int i = 0; i < n; ++i)
    {
        int x, y, c;
        std::cin >> x >> y >> c;
        x += 1010; // 将坐标偏移到正数范围
        y += 1010;
        insert(x - c, y - c, x + c, y + c, 1);
    }

    // 计算前缀和，将差分数组转换为影响数组
    for (int i = 1; i < N; ++i)
    {
        for (int j = 1; j < N; ++j)
        {
            diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1];
        }
    }

    std::cin >> q;
    // 处理每次查询，并输出结果
    for (int i = 0; i < q; ++i)
    {
        int x, y;
        std::cin >> x >> y;
        x += 1010; // 将查询坐标偏移到正数范围
        y += 1010;
        std::cout << diff[x][y] << '\n';
    }

    return 0;
}
