#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
#include <limits>

using namespace std;

int solve() {
    int n;
    cin >> n;
    unordered_map<int, vector<int>> ans;
    int mm = numeric_limits<int>::max();
    vector<int> high;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        high.push_back(a);
    }
    for (int i : high) {
        int ss = 0;
        for (int j : high) {
            ss += abs(i - j);
        }
        if (ss <= mm) {
            ans[ss].push_back(i);
            mm = ss;
        }
    }
    int res = numeric_limits<int>::min();
    for (int j : ans[mm]) {
        res = max(j, res);
    }
    cout << res << endl;
    return 0;
}

int main() {
    solve();
    return 0;
}
