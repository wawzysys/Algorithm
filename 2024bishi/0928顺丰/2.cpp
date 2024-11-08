#include <bits/stdc++.h>
using namespace std;

// Function to check if a string is camelCase
bool isCamelCase(const string &s)
{
    if (s.empty())
        return false;
    if (!islower(s[0]))
        return false;
    for (char c : s)
    {
        if (!isalpha(c))
            return false;
        if (c == '_')
            return false;
    }
    return true;
}

// Function to check if a string is snake_case
bool isSnakeCase(const string &s)
{
    if (s.empty())
        return false;
    if (s.front() == '_' || s.back() == '_')
        return false;
    for (char c : s)
    {
        if (!(islower(c) || c == '_'))
            return false;
    }
    for (int i = 1; i < s.size(); i++)
    {
        if (s[i] == '_' && s[i - 1] == '_')
            return false;
    }
    return true;
}

// Function to convert camelCase to snake_case
string convertToSnakeCase(const string &s)
{
    string res;
    for (char c : s)
    {
        if (isupper(c))
        {
            res += '_';
            res += tolower(c);
        }
        else
        {
            res += c;
        }
    }
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    while (n--)
    {
        string s;
        cin >> s;
        if (isCamelCase(s))
        {
            string converted = convertToSnakeCase(s);
            cout << converted << "\n";
        }
        else if (isSnakeCase(s))
        {
            cout << s << "\n";
        }
        else
        {
            cout << "indistinct\n";
        }
    }
}
