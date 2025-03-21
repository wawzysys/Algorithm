#include <bits/stdc++.h>
using namespace std;
// typedef int long long;
using pii = pair<int, int>;

const int N = 6E5 + 10;
int n, m, k;
vector<int> v;
pii weapon[N];

struct Node
{
    int l, r;
    int sum, add;
} tr[N << 2];

struct Line
{
    int s, d, h;
    friend bool operator<(const Line &a, const Line &b)
    {
        return a.h < b.h;
    }
} lines[N];

void pushdown(int u)
{
    Node &root = tr[u], &left = tr[u << 1], &right = tr[u << 1 | 1];
    if (root.add)
    {
        left.add += root.add, left.sum += (left.r - left.l + 1) * root.add;
        right.add += root.add, right.sum += (right.r - right.l + 1) * root.add;
        root.add = 0;
    }
}

void pushup(int u)
{
    tr[u].sum = tr[u << 1].sum + tr[u << 1 | 1].sum;
}

void modify(int u, int l, int r, int d)
{
    pushdown(u);
    if (tr[u].l >= l && tr[u].r <= r)
    {
        tr[u].sum += d * (tr[u].r - tr[u].l + 1);
        tr[u].add += d;
    }
    else
    {
        int mid = tr[u].l + tr[u].r >> 1;
        if (l <= mid)
            modify(u << 1, l, r, d);
        if (r > mid)
            modify(u << 1 | 1, l, r, d);
        pushup(u);
    }
}

int query(int u, int x)
{
    if (tr[u].l == tr[u].r)
    {
        return tr[u].sum;
    }
    int mid = tr[u].l + tr[u].r >> 1;
    pushdown(u);
    int sum = 0;
    if (x <= mid)
        sum += query(u << 1, x);
    else
        sum += query(u << 1 | 1, x);
    return sum;
}

void build(int u, int l, int r)
{
    tr[u] = {l, r};
    if (l == r)
    {
        return;
    }
    int mid = l + r >> 1;
    build(u << 1, l, mid);
    build(u << 1 | 1, mid + 1, r);
}

int get(int x)
{
    return lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> k;
    v.push_back(1);
    v.push_back(k + 1);
    for (int i = 1, x, y, w; i <= n; i++)
    {
        cin >> x >> y >> w;
        v.push_back(x + 1);
        v.push_back(x + w + 1);
        lines[i] = {x + 1, x + w + 1, y};
    }
    for (int i = 1; i <= m; i++)
    {
        cin >> weapon[i].first >> weapon[i].second;
        weapon[i].first++;
        v.push_back(weapon[i].first);
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
    build(1, 1, N - 1);
    sort(lines + 1, lines + 1 + n);
    sort(weapon + 1, weapon + 1 + m, [](const pii &a, const pii &b)
         { return a.second < b.second; });
    int now = 1;
    long long ans = 0;
    for (int i = 1; i <= m; i++)
    {
        while (lines[now].h <= weapon[i].second && now <= n)
        {
            int x = get(lines[now].s), y = get(lines[now].d);
            modify(1, x, y, 1);
            now++;
        }
        if (weapon[i].first <= k + 1)
        {
            ans += query(1, get(weapon[i].first));
        }
    }
    cout << ans << '\n';

    return 0;
}