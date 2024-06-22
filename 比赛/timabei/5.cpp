#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_SIZE = 1e6 + 10;
using int64 = long long;
using Pair = pair<int, int>;
int arr[MAX_SIZE], differences[MAX_SIZE];
int64 prefix[MAX_SIZE];

int64 calculate(Pair range)
{
    auto [left, right] = range;
    if (left > right)
        return 0;
    right++;
    int64 count = 1ll * (right - left + 1) * (right - left + 1 + 1) / 2 - (right - left + 1);
    return count;
}

signed main()
{
    // jingsaifeiyangyangtigong
    // 争取上省一
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int num_elements, queries;
    cin >> num_elements >> queries;
    for (int i = 1; i <= num_elements; ++i)
        cin >> arr[i];
    for (int i = 1; i < num_elements; ++i)
        differences[i] = arr[i + 1] - arr[i];

    if (num_elements == 1)
    {
        while (queries--)
            cout << 1 << endl;
        return 0;
    }

    vector<Pair> ranges;
    int size = num_elements;
    for (int i = 1; i < size;)
    {
        int start = i;
        while (i < size && differences[start] == differences[i])
            i++;
        ranges.push_back({start, i - 1});
    }

    prefix[0] = calculate(ranges[0]);
    for (int i = 1; i < ranges.size(); ++i)
        prefix[i] = prefix[i - 1] + calculate(ranges[i]);

    while (queries--)
    {
        int left, right;
        cin >> left >> right;
        int64 result = right - left + 1;
        right--;

        auto it = lower_bound(ranges.begin(), ranges.end(), Pair{left, 0});
        auto it2 = lower_bound(ranges.begin(), ranges.end(), Pair{right + 1, 0});

        if (it == it2)
        {
            result += calculate({left, right});
        }
        else
        {
            it2--;
            auto it_first = it->first;
            auto it2_first = it2->first;
            result += calculate({left, it_first - 1});
            result += calculate({it2_first, right});

            if (it2 != ranges.begin())
            {
                it2--;
                auto back_index = it2 - ranges.begin();
                result += prefix[back_index];

                if (it != ranges.begin())
                {
                    auto front_index = it - ranges.begin() - 1;
                    result -= prefix[front_index];
                }
            }
        }

        cout << result << endl;
    }
}
