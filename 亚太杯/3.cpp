#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    // 初始化输入数据
    // vector<int> nums = {1, 2, 3, 4, 5};
    vector<int> nums = {1, 4, 2, 3, 1, 4};

    // 初始化动态规划表，dp[0]表示以偶数结尾的子数组信息，dp[1]表示以奇数结尾的子数组信息
    vector<vector<int>>
        dp(2, vector<int>(2, 0));
    // 遍历输入的数字列表
    for (int num : nums)
    {
        int a, b, c, d;

        if (num % 2 == 1)
        {                     // 奇数
            a = dp[0][0];     // 偶数结尾的最大长度保持不变
            b = dp[1][0] + 1; // 当前奇数，之前以奇数结尾的长度加1
            c = dp[1][0];     // 奇数结尾的最大长度保持不变
            d = dp[1][1] + 1; // 当前奇数，之前以奇数结尾且包含偶数的长度加1
        }
        else
        {                     // 偶数
            a = dp[0][0] + 1; // 当前偶数，之前以偶数结尾的长度加1
            b = dp[0][1];     // 偶数结尾且包含奇数的最大长度保持不变
            c = dp[0][1] + 1; // 当前偶数，之前以偶数结尾且包含奇数的长度加1
            d = dp[1][1];     // 奇数结尾且包含偶数的最大长度保持不变
        }

        // 更新动态规划表
        dp[0] = {a, b};
        dp[1] = {c, d};
    }

    // 计算并输出结果
    cout << max({dp[0][0], dp[0][1], dp[1][0], dp[1][1]}) << endl;

    return 0;
}
