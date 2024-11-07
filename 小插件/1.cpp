#include <bits\stdc++.h>
using namespace std;
int main()
{
    string s1, s2;
    cin >> s1 >> s2;
    if (s1.size() > s2.size())
        swap(s1, s2);
    int len1 = s1.size(), len2 = s2.size();
    int start = 0, mx = 0;
    vector<vector<int>> dp(len1 + 1, vector<int>(len2 + 1, 0));
    for (int i = 1; i <= len1; i++)
    {
        for (int j = 1; j <= len2; j++)
        {
            if (s1[i - 1] == s2[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            if (dp[i][j] > mx)
            {
                mx = dp[i][j];
                start = i - mx;
            }
        }
    }
    cout << s1.substr(start, mx);
    return 0;
}