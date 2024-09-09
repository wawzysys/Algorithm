#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

const long long mod = 1'000'000'007;

long long mod_pow(long long base, long long exp, long long mod)
{
    long long result = 1;
    while (exp > 0)
    {
        if (exp % 2 == 1)
        {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main()
{
    int T;
    cin >> T;
    for (int _ = 0; _ < T; ++_)
    {
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> a[i];
        }

        long long s = 0;
        long long ans = 0;
        for (int x : a)
        {
            s = max((long long)x, s + x);
            ans = max(ans, s);
        }

        long long tot = accumulate(a.begin(), a.end(), 0LL);
        long long result = (tot - ans + ans * mod_pow(2, k, mod)) % mod;
        cout << result << endl;
    }
    return 0;
}