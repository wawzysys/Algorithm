#include <bits/stdc++.h>
using namespace std;

const int N = 1010;
int n, m, idx;
map<string, int> mp;
struct Node
{
    int to, cnt1, cnt2;
};
int a[N], b[N];
int xx, yy, vis[N];
vector<int> g[N];

int get(string s)
{
    if (!mp.count(s))
    {
        mp[s] = ++idx;
    }
    return mp[s];
}

void dfs(int u)
{
    if (vis[u])
        return;
    vis[u] = 1;
    xx += a[u], yy += b[u];
    for (int x : g[u])
    {
        dfs(x);
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> m >> n;
    set<int> st;
    while (n--)
    {
        string sa, sb;
        int x, y;
        cin >> sa >> sb >> x >> y;
        int tx = get(sa), ty = -1;
        if (sb != "*")
        {
            ty = get(sb);
            g[ty].push_back(tx);
        }
        else
        {
            st.insert(tx);
        }
        if (!x)
        {
            a[tx] += y;
        }
        else
        {
            b[tx] += y;
        }
    }
    int ans = 0;
    for (int x : st)
    {
        xx = 0, yy = 0;
        dfs(x);
        if (xx * 5 + yy * 2 > m)
        {
            ans++;
        }
    }
    cout << ans << '\n';

    return 0;
}