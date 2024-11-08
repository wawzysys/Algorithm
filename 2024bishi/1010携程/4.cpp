#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 200005;
int n, q, a[N];
struct Node
{
    int res[2], len;
} t[N << 2];
void push_up(int i)
{
    t[i].len = t[i << 1].len + t[i << 1 | 1].len;
    for (int op = 0; op < 2; ++op)
    {
        if (t[i << 1].len % 2)
        {
            if (op == 0)
                t[i].res[op] = t[i << 1].res[op] & t[i << 1 | 1].res[op];
            else
                t[i].res[op] = t[i << 1].res[op] | t[i << 1 | 1].res[op];
        }
        else
        {
            if (op == 0)
                t[i].res[op] = t[i << 1].res[op] | t[i << 1 | 1].res[op];
            else
                t[i].res[op] = t[i << 1].res[op] & t[i << 1 | 1].res[op];
        }
    }
}
void build(int i, int l, int r)
{
    if (l == r)
    {
        t[i].res[0] = t[i].res[1] = a[l];
        t[i].len = 1;
        return;
    }
    int m = (l + r) >> 1;
    build(i << 1, l, m);
    build(i << 1 | 1, m + 1, r);
    push_up(i);
}
Node query(int i, int l, int r, int x, int y)
{
    if (x <= l && r <= y)
        return t[i];
    int m = (l + r) >> 1;
    if (y <= m)
        return query(i << 1, l, m, x, y);
    else if (x > m)
        return query(i << 1 | 1, m + 1, r, x, y);
    else
    {
        Node left = query(i << 1, l, m, x, y);
        Node right = query(i << 1 | 1, m + 1, r, x, y);
        Node res;
        res.len = left.len + right.len;
        for (int op = 0; op < 2; ++op)
        {
            if (left.len % 2)
            {
                if (op == 0)
                    res.res[op] = left.res[op] & right.res[op];
                else
                    res.res[op] = left.res[op] | right.res[op];
            }
            else
            {
                if (op == 0)
                    res.res[op] = left.res[op] | right.res[op];
                else
                    res.res[op] = left.res[op] & right.res[op];
            }
        }
        return res;
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> q;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];
    build(1, 1, n);
    while (q--)
    {
        int op, l, r;
        cin >> op >> l >> r;
        Node res = query(1, 1, n, l, r);
        cout << res.res[op - 1] << '\n';
    }
    return 0;
}
