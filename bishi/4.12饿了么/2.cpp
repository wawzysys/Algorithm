#include <bits/stdc++.h>
 
const int inf = 0x3f3f3f3f;
using i64 = long long;

void solve() {
    int n, m;
    std::cin >> n >> m;
    std::vector<int> a(n + 1);
    std::vector<std::vector<int>> sum(26, std::vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        std::cin >> a[i];
        for (int j = 0; j < 26; ++j) {
            sum[j][i] += sum[j][i - 1] + (a[i] >> j & 1);
        }
    }

    int t = 0;

    auto get = [&](int r) {
        int x = 0, l = t;
        for (int i = 0; i < 26; ++i) {
            if (sum[i][r] - sum[i][l - 1]) {
                x |= 1 << i;
            }
        }
        return x;
    };

    for (int i = 0; i < m; ++i) {
        int l, r, k;
        std::cin >> l >> r >> k;
        t = l;
        while (l < r) {
            int mid = l + r >> 1;
            if (get(mid) >= k) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if (get(r) == k) {
            std::cout << r << "\n";
        } else {
            std::cout << -1 << "\n";
        }
    }
}

int main() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);

    solve();

    return 0;
}