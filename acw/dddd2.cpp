#include <bits/stdc++.h>

using namespace std;

const int N = 100010, mod = 1e9 + 7;

int a[N];
array<int, 2> dp[N]; 
vector<int> adj[N];

void dfs(int u, int fa) {
	dp[u][a[u]] = 1;
	for (auto v : adj[u]) {
		if (v == fa) continue;
		dfs(v, u);
		array<int, 2> tmp;
		tmp[0] = tmp[1] = 0;
		for (int i : {0, 1}) {
			for (int j : {0, 1}) {
				if (i + j < 2) {
					tmp[i + j] += 1ll * dp[u][i] * dp[v][j] % mod;
					tmp[i + j] %= mod;
				}
				if (j == 1) {
					tmp[i] += 1ll * dp[u][i] * dp[v][j] % mod;
					tmp[i] %= mod;
				}
			}
		}
		dp[u] = tmp;
		cout << u << " " <<  dp[u][0] << " " << dp[u][1] << endl;
	}	
}

int main() {
	cin.tie(0)->sync_with_stdio(false);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) cin >> a[i];
	for (int i = 1; i < n; i++) {
		int u, v;
		cin >> u >> v;
		adj[u].emplace_back(v);
		adj[v].emplace_back(u);
	}	
	dfs(1, 0);
	for (int i = 1; i <= n; i ++ ){
		cout << "i" << i << " "<<dp[i][0] << " " << dp[i][1] << endl;
	}
	cout << dp[1][1] << '\n';
	return 0;
}
