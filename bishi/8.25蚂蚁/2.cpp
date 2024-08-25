#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 10;
bool f1(int num)
{
    std::set<int> seenDigits;
    while (num > 0)
    {
        int digit = num % 10;
        if (seenDigits.find(digit) != seenDigits.end())
        {
            return false;
        }
        seenDigits.insert(digit);
        num /= 10;
    }
    return true;
}
bool f5(int n)
{
    std::unordered_set<char> digits;
    std::string str = std::to_string(n);
    for (char digit : str)
    {
        if (digits.find(digit) != digits.end())
        {
            return false;
        }
        digits.insert(digit);
    }
    return true;
}
int f4(int x)
{
    while (true)
    {
        if (f5(x))
        {
            return x;
        }
        x++;
    }
}

std::vector<int> f2()
{
    std::vector<int> nums;
    for (int i = 1; i <= N; ++i)
    {
        if (f1(i))
        {
            nums.push_back(i);
        }
    }
    return nums;
}

int f3(int x, const std::vector<int> &nums)
{
    auto it = std::lower_bound(nums.begin(), nums.end(), x);
    return it != nums.end() ? *it : -1;
}

int main()
{
    std::vector<int> nums = f2();
    std::sort(nums.begin(), nums.end());

    int T, x;
    std::cin >> T;

    while (T--)
    {
        std::cin >> x;
        if (x > N)
        {
            x = f4(x);
            std::cout << x << std::endl;
        }
        else
        {
            std::cout << f3(x, nums) << std::endl;
        }
    }

    return 0;
}
