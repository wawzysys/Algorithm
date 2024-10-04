#include <bits\stdc++.h>
using namespace std;
int n, m, k, q, i, j, x, y, nx, ny, id, cnt = 0;
char s[15], c;
map<string, int> mp;
struct E
{
    string n;
    int sz, x, y;
    bool al;
} e[20005];
int g[505][505];
int dx[128], dy[128];
int cmp(int a, int b)
{
    if (e[a].sz != e[b].sz)
        return e[a].sz > e[b].sz ? a : b;
    return e[a].n > e[b].n ? a : b;
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
        e[id] = {str, 1, x, y, true};
        if (g[x][y])
        {
            int oid = g[x][y];
            int wid = cmp(id, oid);
            int lid = wid == id ? oid : id;
            e[lid].al = false;
            e[wid].sz += e[lid].sz;
            g[x][y] = wid;
        }
        else
        {
            g[x][y] = id;
        }
    }
    scanf("%d", &q);
    while (q--)
    {
        scanf("%s %c", s, &c);
        string str = s;
        if (!mp.count(str) || !e[mp[str]].al)
        {
            puts("unexisted empire.");
            continue;
        }
        id = mp[str];
        x = e[id].x;
        y = e[id].y;
        nx = x + dx[c];
        ny = y + dy[c];
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
            e[id].sz++;
            g[nx][ny] = id;
            puts("vanquish!");
        }
        else if (oid == id)
        {
            e[id].x = nx;
            e[id].y = ny;
            puts("peaceful.");
        }
        else
        {
            int wid = cmp(id, oid);
            int lid = wid == id ? oid : id;
            e[wid].sz += e[lid].sz;
            e[lid].al = false;
            for (i = 1; i <= n; i++)
                for (j = 1; j <= m; j++)
                    if (g[i][j] == lid)
                        g[i][j] = wid;
            if (wid == id)
            {
                e[id].x = nx;
                e[id].y = ny;
            }
            printf("%s wins!\n", e[wid].n.c_str());
        }
    }
    return 0;
}
