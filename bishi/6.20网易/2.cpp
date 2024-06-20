#include <iostream>
#include <algorithm>

using namespace std;
const int N = 55;

long long f[N][N][N];

int main()
{
    int n, A, B, C;
    cin >> n >> A >> B >> C;

    for (int i = 1; i <= n; i++)
    {
        int a, b, c, v;
        cin >> a >> b >> c >> v;
        for (int j = A; j >= a; j--)
        {
            for (int k = B; k >= b; k--)
            {
                for (int t = C; t >= c; t--)
                {
                    f[j][k][t] = max(f[j][k][t], f[j - a][k - b][t - c] + v);
                }
            }
        }
    }

    cout << f[A][B][C] << "\n";

    return 0;
}
