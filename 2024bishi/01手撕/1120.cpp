#include <bits/stdc++.h>
using namespace std;

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    vector<int> nums = {1, 5, 11, 5};
    int n = nums.size(), m = 0;
    for (int x : nums)
        m += x;
    if (m % 2)
        return false;
    m /= 2;
    vector<bool> f(m + 1);
    f[0] = true;
    for (int i = 1; i <= n; i++)
        for (int j = m; j >= nums[i - 1]; j--)
            f[j] = f[j] | f[j - nums[i - 1]];
    cout << f[m] << endl;

    return 0;
}
