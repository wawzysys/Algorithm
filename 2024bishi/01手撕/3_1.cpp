#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    vector<tuple<int, int, int>> t;
    for (int m = 2; m <= 150; m++)
        for (int n = 1; n < m; n++)
        {
            if ((m - n) % 2 == 1 && gcd(m, n) == 1)
            {
                int a = m * m - n * n, b = 2 * m * n, c = m * m + n * n;
                if (a > b)
                    swap(a, b);
                int k = 1;
                while (a * k + b * k + c * k <= 10000)
                {
                    t.emplace_back(a * k, b * k, c * k);
                    k++;
                }
            }
        }
    sort(t.begin(), t.end(), [&](const tuple<int, int, int> &x, const tuple<int, int, int> &y) -> bool
         {
        int sx = get<0>(x) + get<1>(x) + get<2>(x);
        int sy = get<0>(y) + get<1>(y) + get<2>(y);
        if(sx != sy) return sx < sy;
        return x < y; });
    vector<tuple<int, int, int>> res(10001, {0, 0, 0});
    int cur = 1;
    tuple<int, int, int> last = {0, 0, 0};
    for (auto &[a, b, c] : t)
    {
        int s = a + b + c;
        while (cur <= s && cur <= 10000 && res[cur] == make_tuple(0, 0, 0))
        {
            res[cur] = {a, b, c};
            last = res[cur];
            cur++;
        }
        if (cur > 10000)
            break;
    }
    while (cur <= 10000)
    {
        res[cur] = last;
        cur++;
    }
    int q;
    cin >> q;
    while (q--)
    {
        int k;
        cin >> k;
        cout << get<0>(res[k]) << ' ' << get<1>(res[k]) << ' ' << get<2>(res[k]) << "\n";
    }
}
