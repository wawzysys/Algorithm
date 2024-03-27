#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;

struct SCC {
    int n;
    std::vector<std::vector<int>> adj;
    std::vector<int> stk;
    std::vector<int> dfn, low, bel;
    int cur, cnt;

    SCC() {}
    SCC(int n) {
        init(n);
    }

    void init(int n) {
        this->n = n;
        adj.assign(n, {});
        dfn.assign(n, -1);
        low.resize(n);
        bel.assign(n, -1);
        stk.clear();
        cur = cnt = 0;
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
    }

    void dfs(int x) {
        dfn[x] = low[x] = cur++;
        stk.push_back(x);

        for (auto y : adj[x]) {
            if (dfn[y] == -1) {
                dfs(y);
                low[x] = std::min(low[x], low[y]);
            } else if (bel[y] == -1) {
                low[x] = std::min(low[x], dfn[y]);
            }
        }

        if (dfn[x] == low[x]) {
            int y;
            do {
                y = stk.back();
                bel[y] = cnt;
                stk.pop_back();
            } while (y != x);
            cnt++;
        }
    }
    std::vector<int> work() {
        for (int i = 0; i < n; ++i) {
            if (dfn[i] == -1) {
                dfs(i);
            }
        }
        return bel;
    }
};

void solve() {
    int n, m, x, V;
    std::cin >> n >> m >> V >> x;
 	std::vector<int> a(n), b(n), c(n);
    
    SCC scc(n);

    for (int i = 0; i < n - 1; ++i) {
    	int t;
    	std::cin >> a[i] >> b[i] >> c[i] >> t;
    	for (int j = 0; j < t; ++j) {
    		int k;
    		std::cin >> k;
            scc.addEdge(i, k - 1);
    	}
    }
    std::vector<std::vector<std::vector<int>>> dp(n, std::vector<std::vector<int>>(m + 1, std::vector<int>(V + 1)));

    scc.work();
    std::vector<std::vector<int>> adj(n);
    std::vector<std::vector<int>> has(n);
    for (int i = 0; i < n; ++i) {
        has[scc.bel[i]].push_back(i);
        for (auto j : scc.adj[i]) {
            if (scc.bel[i] != scc.bel[j]) {
                adj[scc.bel[i]].push_back(scc.bel[j]);
            }
        }
        int y = scc.bel[i];
        for (int j = m; j >= a[i]; --j) {
            for (int k = V; k >= b[i]; --k) {
                dp[y][j][k] = std::max(dp[y][j][k], dp[y][j - a[i]][k - b[i]] + c[i] - a[i]);
            }
        }
    }
    


    std::function<void(int, int)> dfs = [&](int u, int fa) {
    	for (auto v : adj[u]) {
    		if (v == fa) continue;
            int now = 0;
            for (int i = m; i >= 0; --i) {
                for (int j = V; j >= 0; --j) {
                    dp[v][i][j] = std::max(dp[v][i][j], dp[u][i][j]);
                    if (i >= a[v] and j >= b[v]) {
                        dp[v][i][j] = std::max(dp[v][i][j], dp[u][i - a[v]][j - b[v]] + c[v] - a[v]);
                        now = std::max(now, dp[v][i][j]);
                    }
                }
            }
    		dfs(v, u);
    	}
    };

    dfs(scc.bel[x - 1], -1);
    int ans = 0;
    for (int i = 0; i <= m; ++i) {
        for (int j = 0; j <= V; ++j) {
            ans = std::max(ans, dp[scc.bel[n - 1]][i][j]);
        }
    }
    std::cout << ans << "\n";
}

int main() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    
    solve();

    return 0;
}
