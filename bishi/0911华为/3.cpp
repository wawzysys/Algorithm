#include <iostream>
#include <vector>
#include <algorithm>

class Solution
{
public:
    int f(std::vector<std::vector<int>> &boxes)
    {
        std::vector<std::vector<int>> a;
        for (const auto &box : boxes)
        {
            int l = box[0], w = box[1], h = box[2];
            a.push_back({l, w, h});
            a.push_back({w, h, l});
            a.push_back({h, l, w});
        }

        std::sort(a.begin(), a.end(), [](const std::vector<int> &a, const std::vector<int> &b)
                  {
            if (a[0] == b[0]) return a[1] > b[1];
            return a[0] > b[0]; });

        int n = a.size();
        std::vector<int> dp(n, 0);

        for (int i = 0; i < n; ++i)
        {
            dp[i] = a[i][2];
        }

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (a[j][0] > a[i][0] && a[j][1] > a[i][1] && a[j][2] > a[i][2])
                {
                    dp[i] = std::max(dp[i], dp[j] + a[i][2]);
                }
            }
        }

        return *std::max_element(dp.begin(), dp.end());
    }
};

int main()
{
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> boxes(n, std::vector<int>(3));
    for (int i = 0; i < n; ++i)
    {
        std::cin >> boxes[i][0] >> boxes[i][1] >> boxes[i][2];
    }

    Solution solution;
    std::cout << solution.f(boxes) << std::endl;

    return 0;
}