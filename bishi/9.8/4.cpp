#include <bits/stdc++.h>
using namespace std;

int fn(vector<vector<int>> &a, int b, int c, int d)
{
    int e = a.size(), f = a[0].size();
    vector<vector<int>> p(e + 1, vector<int>(f + 1, 0));

    for (int i = 0; i < e; i++)
    {
        for (int j = 0; j < f; j++)
        {
            int m = __gcd(a[i][j], b);
            m = m > 1 ? 1 : 0;
            p[i + 1][j + 1] = p[i + 1][j] + p[i][j + 1] - p[i][j] + m;
        }
    }

    int r = 0;
    for (int x = 0; x + c <= e; x++)
    {
        for (int y = 0; y + d <= f; y++)
        {
            int n = p[x + c][y + d] - p[x][y + d] - p[x + c][y] + p[x][y];
            if (n == c * d)
            {
                r++;
            }
        }
    }

    return r;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t;
    cin >> t;
    while (t-- > 0)
    {
        int k, l, q;
        cin >> k >> l >> q;
        vector<vector<int>> a(k, vector<int>(l));
        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < l; j++)
            {
                cin >> a[i][j];
            }
        }

        while (q-- > 0)
        {
            int h1, w1;
            int v;
            cin >> h1 >> w1 >> v;
            int result = fn(a, v, h1, w1);
            cout << result << endl;
        }
    }

    return 0;
}