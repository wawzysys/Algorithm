#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;

template <typename T>
struct Fenwick {
    int n;
    std::vector<T> a;
    
    Fenwick(int n = 0) {
        init(n);
    }
    
    void init(int n) {
        this->n = n;
        a.assign(n, T());
    }
    
    void add(int x, T v) {
        for (int i = x + 1; i <= n; i += i & -i) {
            a[i - 1] += v;
        }
    }
    
    T sum(int x) {
        auto ans = T();
        for (int i = x; i > 0; i -= i & -i) {
            ans += a[i - 1];
        }
        return ans;
    }
    
    T rangeSum(int l, int r) {
        return sum(r) - sum(l);
    }
};

void solve() {
    int n;
    std::cin >> n;
    std::vector<int> a(n + 1), s(n + 1), b{1};
    for (int i = 1; i <= n; ++i) {
        std::cin >> a[i];
        s[i] = s[i - 1] + (a[i] == 2);
        b.push_back(2 * s[i] - i);
    }

    i64 ans = i64(n) * (n + 1) / 2;
    std::sort(b.begin(), b.end());
    b.erase(std::unique(b.begin(), b.end()), b.end());

    auto find = [&](int x) {
        return std::lower_bound(b.begin(), b.end(), x) - b.begin();
    };

    Fenwick<int> tr(2 * n + 1);
    tr.add(find(1), 1);

    for (int i = 1; i <= n; ++i) {
        int now = find(2 * s[i] - i);
        ans += tr.sum(now + 1);
        tr.add(find(2 * s[i] - i + 1), 1);
    }
    std::cout << ans << "\n";
}

int main() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    
    solve();

    return 0;
}