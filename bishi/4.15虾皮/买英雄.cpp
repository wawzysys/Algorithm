#include <bits/stdc++.h>
using namespace std;

const int INF = 1 << 30;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w, n;
    cin >> w >> n;
    vector<pair<int, int>> a(n + 1);
    vector<int> b(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i].first;
        a[i].second = i;
        b[i] = a[i].first;
    }
    sort(a.rbegin(), a.rend() - 1);
    vector<vector<int>> dp(n + 1, vector<int>(w + 1));
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= w; j++) {
            dp[i][j] = max(dp[i][j], dp[i - 1][j]);
            if (j - a[i].first >= 0) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i].first] + 1);
            }
        }
    }
    int now = dp[n][w];
    vector<int> ans;
    for (int i = n; i >= 1; i--) {
        if (w - a[i].first >= 0 && dp[i - 1][w - a[i].first] + 1 == now) {
            now--;
            w -= a[i].first;
            ans.push_back(a[i].second);
        }
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++) {
        cout << b[ans[i]] << ' ';
    }

    return 0;
}