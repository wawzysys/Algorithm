#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main()
{
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    unordered_map<char, vector<pair<int, int>>> d;
    int last = 0;
    int cur = 0;

    for (int i = 1; i < n; ++i)
    {
        if (s[i] != s[i - 1])
        {
            d[s[i - 1]].push_back({last, i - 1});
            last = i;
        }
    }
    d[s[n - 1]].push_back({last, n - 1});

    int ans = INT_MIN;
    for (auto &p : d)
    {
        cur = 0;
        for (auto &range : p.second)
        {
            cur += (range.second - range.first + 1) / k;
        }
        ans = max(ans, cur);
    }

    cout << ans << endl;
    return 0;
}
