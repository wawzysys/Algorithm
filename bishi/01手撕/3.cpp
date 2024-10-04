#include <bits/stdc++.h>
using namespace std;
int q, k, ms = 50000;
vector<int> a(ms + 2, -1), b(ms + 2), c(ms + 2), sum(ms + 2, 1e9);
int gcd(int x, int y) { return y ? gcd(y, x % y) : x; }
int main()
{
    for (int m = 2; m <= 300; m++)
        for (int n = 1; n < m; n++)
            if ((m - n) % 2 && gcd(m, n) == 1)
            {
                int x = m * m - n * n, y = 2 * m * n, z = m * m + n * n, s = x + y + z;
                if (x > y)
                    swap(x, y);
                for (int k = 1; k * s <= ms; k++)
                {
                    int s1 = k * s;
                    int x1 = k * x, y1 = k * y, z1 = k * z;
                    if (a[s1] == -1 || (a[s1] > x1) || (a[s1] == x1 && b[s1] > y1) || (a[s1] == x1 && b[s1] == y1 && c[s1] > z1))
                    {
                        a[s1] = x1;
                        b[s1] = y1;
                        c[s1] = z1;
                        sum[s1] = s1;
                    }
                }
            }
    a[ms + 1] = 1e9;
    sum[ms + 1] = 1e9;
    for (int i = ms; i >= 1; i--)
    {
        if (a[i] == -1 || sum[i] > sum[i + 1] || (sum[i] == sum[i + 1] && ((a[i] > a[i + 1]) || (a[i] == a[i + 1] && b[i] > b[i + 1]) || (a[i] == a[i + 1] && b[i] == b[i + 1] && c[i] > c[i + 1]))))
        {
            a[i] = a[i + 1];
            b[i] = b[i + 1];
            c[i] = c[i + 1];
            sum[i] = sum[i + 1];
        }
    }
    scanf("%d", &q);
    while (q--)
    {
        scanf("%d", &k);
        printf("%d %d %d\n", a[k], b[k], c[k]);
    }
}
