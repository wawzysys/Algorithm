#include <bits/stdc++.h>
using namespace std;

const int N = 1E5 + 10;
vector<int> g[N], ans;
int vis[N], cnt;

void dfs(int u) {
    vis[u] = 1;
    cnt++;
    for (int x : g[u]) {
        if (!vis[x]) {
            dfs(x);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    for (int i = 1, x, y; i <= m; i++) {
        cin >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    for (int i = 1; i <= n; i++) {
        if (!vis[i]) {
            cnt = 0;
            dfs(i);
            ans.push_back(cnt);
        }
    }
    if ((int)ans.size() != 2) {
        cout << "0\n";
    } else {
        cout << 1LL * ans[0] * ans[1] << '\n';
    }

    return 0;
}