#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;
    vector<int> abc(n + 1, 0);
    for (int i = 1; i <= n; ++i)
    {
        abc[i] = abc[i - 1] + (s[i - 1] == '0' ? 1 : 0);
    }

    string result;
    result.reserve(q);

    for (int i = 0; i < q; ++i)
    {
        int l, r, k;
        cin >> l >> r >> k;
        int cnt0 = abc[r] - abc[l - 1];
        if (k <= cnt0)
        {
            result += '0';
        }
        else
        {
            result += '1';
        }
    }

    cout << result;
}
