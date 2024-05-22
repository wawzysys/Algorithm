#include <bits/stdc++.h>
using namespace std;

void solve(const int *list1, int len1, const int *list2, int len2)
{
    int maxLen = 0;
    int endIdx1 = -1;

    for (int i = 0; i < len1; ++i)
    {
        for (int j = 0; j < len2; ++j)
        {
            int k = 0;
            while (i + k < len1 && j + k < len2 && list1[i + k] == list2[j + k])
            {
                ++k;
            }
            if (k > maxLen)
            {
                maxLen = k;
                endIdx1 = i + k - 1;
            }
        }
    }

    if (maxLen == 0)
    {
        cout << "-1" << endl;
        return;
    }
    else
    {
        string result;
        for (int i = endIdx1 - maxLen + 1; i <= endIdx1; ++i)
        {
            if (!result.empty())
            {
                result += " ";
            }
            result += to_string(list1[i]);
        }
        cout << result << endl;
        return;
    }
}
void init()
{
    string input1, input2;
    getline(cin, input1);
    getline(cin, input2);

    istringstream stream1(input1);
    istringstream stream2(input2);

    vector<int> a;
    vector<int> b;
    int number;
    while (stream1 >> number)
    {
        a.push_back(number);
    }
    while (stream2 >> number)
    {
        b.push_back(number);
    }

    solve(a.data(), a.size(), b.data(), b.size());
}
int main()
{
    init();
    return 0;
}
