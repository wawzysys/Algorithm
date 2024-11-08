#include <bits/stdc++.h>
using namespace std;

const int INF = 1 << 30;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w, n;
    cin >> w >> n;
    vector<pair<int, int>> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }
    sort(a.begin() + 1, a.end());
    vector<vector<int>> dp(n + 1, vector<int>(w + 1, INF));
    vector<int> pre(n + 1);
    dp[0][0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= w; j++) {
            dp[i][j] = min(dp[i][j], dp[i - 1][j]);
            if (j - a[i].first >= 0) {
                dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i].first] + 1);
            }
        }
    }
    vector<int> vis(n + 1);
    int now = w;
    for (int i = n; i >= 1; i--) {
        if (now - a[i].first >= 0 && dp[i - 1][now - a[i].first] != INF) {
            vis[a[i].second] = 1;
            now -= a[i].first;
        }
    }
    for (int i = 1; i <= n; i++) {
        cout << vis[i] << " \n"[i == n];
    }

    return 0;
}
/*
10 5
5 2 6 4 3
*/