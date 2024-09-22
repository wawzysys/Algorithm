#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (auto &x : a)
            cin >> x;
        unordered_set<long long> s(a.begin(), a.end());
        int U = s.size();
        bool has0 = s.find(0) != s.end();

        if (has0)
        {
            if (U <= n)
                cout << "yes\n";
            else
                cout << "no\n";
        }
        else
        {
            if (U + 1 <= n)
                cout << "yes\n";
            else
                cout << "no\n";
        }
    }
}

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

void solve()
{
    int t;
    cin >> t; // 读取测试用例的数量
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            a[i] = abs(a[i]); // 转换为绝对值
        }

        set<int> st(a.begin(), a.end()); // 使用集合去重
        if (st.count(0) || a.size() != st.size())
        {
            cout << "yes" << endl;
        }
        else
        {
            sort(a.begin(), a.end()); // 对数组进行排序
            bool ok = false;
            // 三重循环寻找 a[i] + a[j] == a[k]
            for (int i = 0; i < n - 2; i++)
            {
                for (int j = i + 1; j < n - 1; j++)
                {
                    for (int k = j + 1; k < n; k++)
                    {
                        if (a[i] + a[j] == a[k])
                        {
                            ok = true;
                        }
                    }
                }
            }
            cout << (ok ? "yes" : "no") << endl;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}

// 这个是飞给的