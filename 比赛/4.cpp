#include <iostream>
using namespace std;

int n, k, m;
int *dp;

int main()
{
    cin >> n >> k;
    dp = new int[k + 1]();
    while (dp[k] < n)
    {
        m++;
        for (int i = k; i >= 1; i--)
            dp[i] += dp[i - 1] + 1;
    }
    cout << m << endl;
    delete[] dp;
    return 0;
}
