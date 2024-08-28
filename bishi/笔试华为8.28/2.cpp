#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    int ans = 1e9;
    for (int i = 0; i < n; ++i)
    {
        cin >> nums[i];
        if (ans > nums[i])
        {
            ans = nums[i];
        }
    }
    int m;
    cin >> m;
    unordered_map<int, int> mo;
    for (int c : nums)
    {
        int tt = c % m;
        mo[tt]++;
        ans = max(ans, mo[tt]);
    }
    sort(nums.begin(), nums.end());
    for (int c : nums)
    {
        if (mo[c % m] == ans)
        {
            cout << c << endl;
            break;
        }
    }
    return 0;
}