#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
template <typename T>
vector<T> input()
{
    vector<T> a;
    T s;
    while (cin >> s)
    {
        a.push_back(s);
        if (cin.get() != ' ')
            break;
    }
    return a;
}
void solve()
{
    vector<int> nums = input<int>();
    vector<int> st;
    vector<int> ans;

    for (int a : nums)
    {
        if (!st.empty() && find(st.begin(), st.end(), a) != st.end())
        {
            while (st.back() != a)
            {
                ans.push_back(st.back());
                st.pop_back();
            }
            ans.push_back(st.back());
            st.pop_back();
        }
        st.push_back(a);
    }

    while (!st.empty())
    {
        ans.push_back(st.back());
        st.pop_back();
    }

    for (size_t i = 0; i < ans.size(); ++i)
    {
        cout << ans[i];
        if (i != ans.size() - 1)
            cout << " ";
    }
    cout << endl;
}

int main()
{
    solve();
    return 0;
}
