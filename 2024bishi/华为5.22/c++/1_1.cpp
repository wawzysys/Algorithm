#include <bits/stdc++.h>
using namespace std;
template <typename T>
std::vector<T> input()
{
    std::vector<T> a;
    T s;
    while (std::cin >> s)
    {
        a.push_back(s);
        if (std::cin.get() != ' ')
            break;
    }
    return a;
}
void slove(const vector<int> &list1, const vector<int> &list2)
{
    int len1 = list1.size();
    int len2 = list2.size();
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
    }
    else
    {
        // string result;
        for (int i = endIdx1 - maxLen + 1; i <= endIdx1; ++i)
        {
            cout << list1[i] << " \n"[i == endIdx1];
        }
    }
}
int main()
{
    std::vector<int> a = input<int>();
    std::vector<int> b = input<int>();
    slove(a, b);
    return 0;
}