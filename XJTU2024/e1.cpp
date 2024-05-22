#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e6 + 10;
signed main()
{
    int n;
    cin >> n;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        // st.insert(i);
    }
    map<int, int> next;
    next[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        int u = next[a[i]];
        next[i] = u;
        next[a[i]] = i; // 插进去
        for (auto x : next)
        {
            cout << x.first << " :" << x.second << endl;
        }
        cout << endl;
    }
    int i = 0;
    while (next[i] != 0)
    {
        cout << next[i] << " ";
        i = next[i];
    }
}