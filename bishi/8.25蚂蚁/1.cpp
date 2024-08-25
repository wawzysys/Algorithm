#include <iostream>
using namespace std;
string solve(int a, int b, int c, int d)
{
    if (d != 0 and a == 0)
    {
        return "NO";
    }
    if (d != 0 and b == 0)
    {
        return "NO";
    }
    if (a != b)
    {
        return "NO";
    }
    if (d > a || d > b)
    {
        return "NO";
    }
    return "YES";
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        cout << solve(a, b, c, d) << endl;
    }
    return 0;
}
