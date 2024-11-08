#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_N = 100005;
int nums1[MAX_N];
int nums2[MAX_N];
int count_nums[MAX_N];

int main()
{
    int n;
    scanf("%d", &n);

    // 读取数组
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &nums1[i]);
    }

    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &nums2[i]);
    }

    vector<int> positions;
    vector<int> values;

    // 收集 nums1[i] == nums2[i] 的位置和对应的值
    for (int i = 0; i < n; ++i)
    {
        if (nums1[i] == nums2[i])
        {
            positions.push_back(i);
            values.push_back(nums2[i]);
            count_nums[nums2[i]]++;
        }
    }

    int l = positions.size();

    if (l == 0)
    {
        printf("0\n");
        return 0;
    }

    // 检查是否存在某个值出现次数超过一半
    bool possible = true;
    for (int i = 1; i <= 100000; ++i)
    {
        if (count_nums[i] > l / 2)
        {
            possible = false;
            break;
        }
    }

    if (!possible)
    {
        printf("-1\n");
        return 0;
    }

    // 重新排列值，旋转 l/2 位
    int offset = l / 2;
    vector<int> assigned_values(l);

    for (int i = 0; i < l; ++i)
    {
        assigned_values[i] = values[(i + offset) % l];
        if (nums1[positions[i]] == assigned_values[i])
        {
            // 如果出现 nums1[i] == nums2[i]，说明不可行
            possible = false;
            break;
        }
    }

    if (!possible)
    {
        printf("-1\n");
        return 0;
    }

    // 计算总代价
    long long total_cost = 0;
    for (int i = 0; i < l / 2; ++i)
    {
        int pos_i = positions[i];
        int pos_j = positions[i + offset];
        total_cost += pos_i + pos_j;
    }

    printf("%lld\n", total_cost);

    return 0;
}
