#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_N 100

typedef struct
{
    int x, y;
} Point;

int N, K;
int grid[MAX_N][MAX_N];
int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int sint()
{
    int value;
    scanf("%d", &value);
    return value;
}

void mint(int *values, int count)
{
    for (int i = 0; i < count; i++)
    {
        scanf("%d", &values[i]);
    }
}

bool check(int P)
{
    if (grid[0][0] > P || grid[N - 1][N - 1] > P)
    {
        return false;
    }

    bool visited[MAX_N][MAX_N] = {false};
    Point queue[MAX_N * MAX_N];
    int front = 0, rear = 0;

    queue[rear++] = (Point){0, 0};
    visited[0][0] = true;
    int steps = 0;

    while (front < rear && steps <= K)
    {
        int size = rear - front;
        for (int i = 0; i < size; i++)
        {
            Point p = queue[front++];
            int x = p.x, y = p.y;

            if (x == N - 1 && y == N - 1)
            {
                if (steps <= K)
                {
                    return true;
                }
            }

            for (int j = 0; j < 4; j++)
            {
                int nx = x + dir[j][0], ny = y + dir[j][1];
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && grid[nx][ny] <= P)
                {
                    visited[nx][ny] = true;
                    queue[rear++] = (Point){nx, ny};
                }
            }
        }
        steps++;
    }

    return false;
}

int main()
{
    N = sint();
    K = sint();

    int mm = 0;
    int max_value = 0;

    for (int i = 0; i < N; i++)
    {
        int row[MAX_N];
        mint(row, N);
        for (int j = 0; j < N; j++)
        {
            grid[i][j] = row[j];
            if (i == 0 && j == 0)
            {
                mm = grid[i][j];
            }
            if (grid[i][j] > max_value)
            {
                max_value = grid[i][j];
            }
        }
    }

    int l = mm;
    int r = max_value;

    while (l < r)
    {
        int mid = (l + r) / 2;
        if (check(mid))
        {
            r = mid;
        }
        else
        {
            l = mid + 1;
        }
    }

    printf("%d\n", l);

    return 0;
}