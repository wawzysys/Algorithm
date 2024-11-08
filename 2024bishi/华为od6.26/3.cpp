#include <bits\stdc++.h>
using namespace std;
int getResult(int flaw, const string &s)
{
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    vector<int> idxs;
    for (int i = 0; i < s.length(); i++)
    {
        if (vowels.find(s[i]) != vowels.end())
        {
            idxs.push_back(i);
        }
    }
    int ans = 0;
    int l = 0, r = 0;
    int n = idxs.size();
    while (r < n)
    {
        int diff = idxs[r] - idxs[l] - (r - l);
        if (diff > flaw)
        {
            l++;
        }
        else if (diff < flaw)
        {
            r++;
        }
        else
        {
            ans = max(ans, idxs[r] - idxs[l] + 1);
            r++;
        }
    }
    return ans;
}
int main()
{
    int flaw;
    string s;
    cin >> flaw >> s;
    cout << getResult(flaw, s) << endl;
    return 0;
}
