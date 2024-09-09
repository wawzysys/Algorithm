#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    string t;
    cin >> n >> t;

    unordered_map<int, int> cnt;
    cnt[0] = -1;
    int s = 0;
    int ans = 0;

    for (int i = 0; i < n; ++i)
    {
        char c = t[i];
        if (c == 'A')
        {
            s += 1;
        }
        else
        {
            s -= 1;
        }

        if (cnt.find(s) == cnt.end())
        {
            cnt[s] = i;
        }
        else
        {
            ans = max(ans, i - cnt[s]);
        }
    }

    cout << ans << endl;
    return 0;
}