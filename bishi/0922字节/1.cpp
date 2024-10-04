#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;

    vector<int> f(n, 0); // 用于存储翻转标志
    int sum_f = 0;       // 记录当前翻转操作的次数

    // 初始化翻转标志
    for (int i = 0; i < n; ++i)
    {
        if (s[i] == '1')
        {
            f[i] = 1;
            sum_f += 1;
        }
    }

    // 如果翻转次数超过k，进行调整
    if (sum_f > k)
    {
        for (int i = n - 1; i >= 0; --i)
        {
            if (f[i] == 1)
            {
                f[i] = 0;
                sum_f -= 1;
                if (sum_f == k)
                {
                    break;
                }
            }
        }
    }

    // 如果需要，调整奇偶性
    if ((k - sum_f) % 2 == 1)
    {
        f[n - 1] = 1 - f[n - 1];
        sum_f += (f[n - 1] == 1) ? 1 : -1;
    }

    // 剩余的翻转次数
    int rem = k - sum_f;
    if (rem < 0 || rem % 2 != 0)
    {
        // 剩余的翻转可以通过偶数次翻转来调整
        // 不需要执行额外操作
    }

    // 应用翻转并输出结果
    string result;
    for (int i = 0; i < n; ++i)
    {
        int s_i = s[i] - '0';       // 将字符转换为整数
        int s_i_prime = s_i ^ f[i]; // 通过异或操作进行翻转
        result += to_string(s_i_prime);
    }

    cout << result << endl;

    return 0;
}
