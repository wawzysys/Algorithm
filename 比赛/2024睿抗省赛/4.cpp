#include <bits/stdc++.h>
using namespace std;
struct J
{
    int t, de, pr;
};
bool compare(J a, J b)
{
    return a.de < b.de;
}
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        vector<J> jobs(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> jobs[i].t >> jobs[i].de >> jobs[i].pr;
        }
        sort(jobs.begin(), jobs.end(), compare);
        // for (auto x : jobs)
        // {
        //     cout << x.t << " " << x.de << " " << x.pr << endl;
        // }
        vector<int> dp(5001, 0);
        for (int i = 0; i < n; ++i)
        {
            int a = jobs[i].pr, b = jobs[i].t, c = jobs[i].de;
            for (int j = c - b; j >= 0; --j)
                dp[j + b] = max(dp[j] + a, dp[j + b]);
        }

        int mm = -1;
        for (auto c : dp)
        {
            mm = max(mm, c);
        }
        cout << mm << endl;
    }
    return 0;
}