#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    string ConvertString(string originalStr)
    {
        string ans = "";
        int count = 0;
        for (int i = 0; i < originalStr.length(); i++)
        {
            char ch = originalStr[i];
            if (ch == '(')
            {
                if (count == 0)
                {
                    ans.push_back('(');
                }
                count++;
            }
            else if (ch == ')')
            {
                count--;
                if (count == 0)
                {
                    ans.push_back('*');
                    ans.push_back(')');
                }
            }
            else
            {
                if (count == 0)
                {
                    ans.push_back(ch);
                }
            }
        }
        return ans;
    }
};
int main()
{
    string originalStr;
    cin >> originalStr;
    Solution s;
    cout << s.ConvertString(originalStr) << endl;
    return 0;
}