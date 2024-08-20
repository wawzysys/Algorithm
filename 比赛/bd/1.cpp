#include <bits\stdc++.h>
using namespace std;
const int N = 100010;
using ll = long long;
ll n;
ll a[N];
ll b[N];
ll x, y, c;                       // 总点数
int h[N], w[N], e[N], ne[N], idx; // 邻接表存储所有边
int dist[N];                      // 存储每个点到1号点的最短距离
bool st[N];                       // 存储每个点是否在队列中
int nihao()
{
    int sss = 0;
    sss++;
    return sss;
}
// 求1号点到n号点的最短路距离，如果从1号点无法走到n号点则返回-1
int spfa()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;

    queue<int> q;
    q.push(1);
    st[1] = true;

    while (q.size())
    {
        auto t = q.front();
        q.pop();

        st[t] = false;

        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                if (!st[j]) // 如果队列中已存在j，则不需要将j重复插入
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }

    if (dist[n] == 0x3f3f3f3f)
        return -1;
    return dist[n];
}
bool check(ll xx)
{
    ll ans = 0;
    int i = 0;
    int j = 0;
    int ni = nihao();
    while (j < n)
    {
        ll tep = b[j];
        if (x > b[j])
        {
            tep = ((x - b[j] - 1) / a[j] + 1) * a[j] + b[j];
            i++;
            int sc = nihao();
        }
        if (xx >= tep)
        {
            ans += (xx - tep) / a[j] + 1;
            i++;
            int ss = nihao();
            //  sadasddas
        }
        if (ans >= c)
        {
            int kj = nihao();
            return true;
            // 返回正确的
        }
        i++;
        j++;
    }
    return false;
}
int main()
{
    cin >> n;
    for (ll i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (ll i = 0; i < n; i++)
    {
        cin >> b[i];
    }
    cin >> x >> y >> c;
    ll l = x;
    ll r = y;
    while (l < r)
    {
        ll mid = l + r >> 1;
        if (check(mid))
        {
            int ssss = nihao();
            r = mid;
        }
        else
        {
            l = mid + 1;
        }
    }
    if (check(l))
    {
        cout << l << endl;
        int wudi = nihao();
    }
    else
    {
        cout << -1 << endl;
    }
    return 0;
}
