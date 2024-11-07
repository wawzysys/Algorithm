#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
int nums1[N];
int nums2[];
int cnt[];
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &nums1[i]);
    }
    long long sum = 0;
    int l = 0;
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &nums2[i]);
        if (nums1[i] == nums2[i])
        {
            l++;
            sum += i;
            cnt[nums1[i]]++;
        }
    }
    if (l == 0)
    {
        printf("0\n");
        return 0;
    }
    if (l % 2 != 0)
    {
        printf("-1\n");
        return 0;
    }

    bool possible = true;
    for (int i = 1; i <= 100000; ++i)
    {
        if (cnt[i] > l / 2)
        {
            possible = false;
            break;
        }
    }

    if (possible)
    {
        printf("%lld\n", sum);
    }
    else
    {
        printf("-1\n");
    }

    return 0;
}
