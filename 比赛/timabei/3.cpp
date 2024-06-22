#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_SIZE = 1e6 + 10, MOD = 998244353;
using int64 = long long;

int64 power(int64 base, int64 exponent)
{
    int64 result = 1;
    while (exponent)
    {
        if (exponent & 1)
            result = result * base % MOD;
        exponent >>= 1;
        base = base * base % MOD;
    }
    return result;
}

#define inverse(x) power(x, MOD - 2)

std::vector<int> factorial(1, 1);
std::vector<int> inverse_factorial(1, 1);

int64 combination(int n, int k)
{
    if (k < 0 || k > n)
        return 0;
    while ((int)factorial.size() < n + 1)
    {
        factorial.push_back(1ll * factorial.back() * (int)factorial.size() % MOD);
        inverse_factorial.push_back(inverse(factorial.back()));
    }
    return 1ll * factorial[n] * inverse_factorial[k] % MOD * inverse_factorial[n - k] % MOD;
}

void compute()
{
    // jingsaifeiyangyangtigong
    // 争取上省一
    int64 x_start, y_start, x_end, y_end, total_steps, probability_p, probability_q;
    cin >> x_start >> y_start >> x_end >> y_end >> total_steps >> probability_p >> probability_q;
    auto delta_x = x_end - x_start, delta_y = y_end - y_start;
    if (delta_x + delta_y != total_steps || delta_x < 0 || delta_y < 0)
    {
        cout << 0;
        return;
    }
    probability_p *= inverse(100);
    probability_p %= MOD;
    probability_q *= inverse(100);
    probability_q %= MOD;
    cout << combination(total_steps, delta_x) * power(probability_p, delta_x) % MOD * power(probability_q, delta_y) % MOD;
}

signed main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0), std::cout.tie(0);
    int test_cases;
    cin >> test_cases;
    while (test_cases--)
    {
        compute();
        cout << '\n';
    }
    return 0;
}