#include <cstdio>
#include <string>
#include <map>
using namespace std;
int n, m, k, q, i, j, x, y, nx, ny, id, cnt = 0;
char s[15], c;
map<string, int> mp;
struct E
{
    string n;
    int x, y;
} e[20005];
int parent[20005], sz[20005];
bool alive[20005];
int g[505][505];
int dx[128], dy[128];

int find(int x)
{
    if (parent[x] != x)
        parent[x] = find(parent[x]);
    return parent[x];
}

int cmp(int a, int b)
{
    a = find(a);
    b = find(b);
    if (sz[a] != sz[b])
        return sz[a] > sz[b] ? a : b;
    if (e[a].n != e[b].n)
        return e[a].n > e[b].n ? a : b;
    return a;
}

int main()
{
    dx['W'] = -1;
    dy['W'] = 0;
    dx['S'] = 1;
    dy['S'] = 0;
    dx['A'] = 0;
    dy['A'] = -1;
    dx['D'] = 0;
    dy['D'] = 1;
    scanf("%d%d%d", &n, &m, &k);
    for (i = 0; i < k; i++)
    {
        scanf("%s%d%d", s, &x, &y);
        string str = s;
        id = ++cnt;
        mp[str] = id;
        parent[id] = id;
        sz[id] = 1;
        alive[id] = true;
        e[id] = {str, x, y};
        if (g[x][y] == 0)
        {
            g[x][y] = id;
        }
        else
        {
            int oid = g[x][y];
            oid = find(oid);
            int wid = cmp(id, oid);
            int lid = wid == id ? oid : id;
            parent[lid] = wid;
            sz[wid] += sz[lid];
            alive[lid] = false;
            g[x][y] = wid;
        }
    }
    scanf("%d", &q);
    while (q--)
    {
        scanf("%s %c", s, &c);
        string str = s;
        if (!mp.count(str))
        {
            puts("unexisted empire.");
            continue;
        }
        id = mp[str];
        id = find(id);
        if (!alive[id])
        {
            puts("unexisted empire.");
            continue;
        }
        x = e[id].x;
        y = e[id].y;
        nx = x + dx[(unsigned char)c];
        ny = y + dy[(unsigned char)c];
        if (nx < 1 || nx > n || ny < 1 || ny > m)
        {
            puts("out of bounds!");
            continue;
        }
        int oid = g[nx][ny];
        if (oid == 0)
        {
            e[id].x = nx;
            e[id].y = ny;
            sz[id]++;
            g[nx][ny] = id;
            puts("vanquish!");
        }
        else
        {
            oid = find(oid);
            if (oid == id)
            {
                e[id].x = nx;
                e[id].y = ny;
                puts("peaceful.");
            }
            else
            {
                int wid = cmp(id, oid);
                int lid = wid == id ? oid : id;
                parent[lid] = wid;
                sz[wid] += sz[lid];
                alive[lid] = false;
                g[nx][ny] = wid;
                if (wid == id)
                {
                    e[id].x = nx;
                    e[id].y = ny;
                }
                printf("%s wins!\n", e[wid].n.c_str());
            }
        }
    }
    return 0;
}
