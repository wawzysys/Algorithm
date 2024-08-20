#include <bits/stdc++.h>

#define int long long

using namespace std;

const int N = 100010;

int n;
char op[3];
map<int, int> pref;
vector<pair<int, int>> vec;

signed main()
{
    scanf("%lld", &n);
    int cur = 0;
    for (int i = 1; i <= n; i++)
    {
        int x;
        scanf("%lld%s", &x, op);
        if (op[0] == 'R')
        {
            pref[cur]++;
            pref[cur + x]--;
            cur = cur + x - 1;
        }
        else
        {
            pref[cur - x + 1]++;
            pref[cur + 1]--;
            cur = cur - x + 1;
        }
    }
    for (auto pr : pref)
    {
        cout << pr.first << " " << pr.second << endl;
        vec.push_back(pr);
    }
    int ans = 0, sum = 0;
    for (int i = 0; i < vec.size(); i++)
    {
        sum = sum + vec[i].second;
        if (sum % 4 == 1)
            ans = ans + vec[i + 1].first - vec[i].first;
    }
    printf("%lld\n", ans);
    return 0;
}