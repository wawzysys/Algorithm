#include <bits/stdc++.h>
#include <string>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
using ll = long long;

int main () {
    ll n; cin >> n;
    vector<int> a(n);
    ll sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum += a[i];
    }
    vector<int> b = a;
    sort(b.begin(), b.end(), greater<int>());
    ll s = n * b[0] - sum;
    for (int i = 0; i < n; ++i) {
        if (a[i] == b[0]) {
            cout << sum << "\n";
            continue;
        }
        if (n == 2) {
            cout << "-1\n";
            continue;
        }
        a[i] += 1;
        ll diff = b[0] - a[i], cur = s - (b[0] - a[i] + 1), ans = sum + 1;
        if (diff <= cur) {
            ans += 2 * diff;
            cout << ans << "\n";
        } else {
            ans += 2 * cur;
            a[i] += cur;
            ll l = 1, r = 1e9;
            while (l <= r) {
                ll mid = (l + r) / 2;
                ll t = mid / (n - 1);
                if (mid % (n - 1)) t += 1;
                if (a[i] + mid < t + b[0]) l = mid + 1;
                else r = mid - 1;
            }
            ans += 2 * l;
            cout << ans << "\n";
        }
    }
}