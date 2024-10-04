#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s1, s2;
    string line;
    getline(cin, line);
    stringstream ss(line);
    ss >> s1 >> s2;
    if (s1.length() != s2.length())
    {
        cout << "false";
        return 0;
    }

    int mapping[26];
    memset(mapping, -1, sizeof(mapping));
    bool used[26];
    memset(used, false, sizeof(used));

    int m = 0;
    int n = 0;
    for (int i = 0; i < s1.length(); ++i)
    {
        char c1 = s1[i];
        char c2 = s2[i];
        if (mapping[c1 - 'a'] == -1)
        {
            mapping[c1 - 'a'] = c2;
            m += 1;
        }
        else
        {
            if (mapping[c1 - 'a'] != c2)
            {
                cout << "false";
                return 0;
            }
        }
        if (!used[c2 - 'a'])
        {
            used[c2 - 'a'] = true;
            n += 1;
        }
    }

    if (n < 26 || m == n)
    {
        cout << "true";
    }
    else
    {
        cout << "false";
    }
}
