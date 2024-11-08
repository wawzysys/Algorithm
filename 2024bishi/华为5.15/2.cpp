#include <bits/stdc++.h>

using namespace std;
string parse_to_ab_pattern(const string &pattern)
{
    int i = 0;
    string result = "";
    while (i < pattern.size())
    {
        if (pattern[i] == 'N')
        {
            result += 'b';
            i++;
        }
        else if (pattern[i] == 'A')
        {
            result += 'a';
            i++;
        }
        else if (isdigit(pattern[i]))
        {
            int j = i;
            while (j < pattern.size() && isdigit(pattern[j]))
            {
                j++;
            }
            int count = stoi(pattern.substr(i, j - i));
            if (pattern[j] == '(')
            {
                int depth = 1;
                int k = j + 1;
                while (k < pattern.size() && depth > 0)
                {
                    if (pattern[k] == '(')
                    {
                        depth++;
                    }
                    else if (pattern[k] == ')')
                    {
                        depth--;
                    }
                    k++;
                }
                string subpattern = parse_to_ab_pattern(pattern.substr(j + 1, k - j - 2));
                for (int c = 0; c < count; ++c)
                {
                    result += subpattern;
                }
                i = k;
            }
            else
            {
                result += "{" + to_string(count) + "}";
                i = j;
            }
        }
        else
        {
            i++;
        }
    }
    return result;
}
uint64_t get_hash(const vector<uint64_t> &h, const vector<uint64_t> &p, int l, int r, uint64_t mod)
{
    uint64_t res = (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod;
    return res;
}

int main()
{
    string pattern;
    cin >> pattern;
    pattern = parse_to_ab_pattern(pattern);
    string s;
    cin >> s;
    string tep = "";
    for (char c : s)
    {
        if (isdigit(c))
        {
            tep += 'b';
        }
        else
        {
            tep += 'a';
        }
    }
    int n = tep.size();
    int n2 = pattern.size();
    uint64_t base = 131;
    uint64_t mod = 1e9 + 7;
    vector<uint64_t> h(n + 1, 0);
    vector<uint64_t> p(n + 1, 1);
    if (n2 > n)
    {
        cout << "!" << endl;
        return 0;
    }
    for (int i = 1; i <= n; ++i)
    {
        p[i] = p[i - 1] * base % mod;
        h[i] = (h[i - 1] * base + tep[i - 1]) % mod;
    }
    vector<uint64_t> h1(n2 + 1, 0);
    for (int i = 1; i <= n2; ++i)
    {
        h1[i] = (h1[i - 1] * base + pattern[i - 1]) % mod;
    }
    bool flag = false;
    for (int i = 1; i <= n - n2 + 1; ++i)
    {
        int j = i + n2 - 1;
        if (j > n)
        {
            break;
        }
        if (get_hash(h, p, i, j, mod) == h1[n2])
        {
            flag = true;
            cout << s.substr(i - 1, n2) << endl;
            break;
        }
    }
    if (!flag)
    {
        cout << "!" << endl;
    }
    return 0;
}
