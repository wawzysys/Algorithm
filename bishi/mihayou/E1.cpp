#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;
const int mod = 1000000007;

i64 qpow(i64 x, i64 y) {
    i64 res = 1;
    for (; y; y /= 2, x = x * x % mod)
        if (y & 1)
            res = res * x % mod;
    return res;
}

void solve() {
       int n, q;
       std::cin >> n >> q;
       std::vector<i64> a(n), cnt(n, q);
       for (int i = 0; i < n; ++i) {
           std::cin >> a[i];
       }
       for (int i = 0; i < q; ++i) {
           int x;
           std::cin >> x;
           cnt[x - 1]--;
       }
       i64 ans = 0;
       for (int i = 0; i < n; ++i) {
           ans += a[i] * qpow(2, cnt[i]);
           ans %= mod;
       }
       std::cout << ans << "\n";
}

int main() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    
    solve();

    return 0;
}

