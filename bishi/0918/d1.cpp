#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;
using PII = std::pair<int, int>;
const int N = 1e5 + 13;

void solve()
{
    int n;
    std::cin >> n;
    std::cout << ((n & (n - 1)) == 0 ? "YES\n" : "NO\n");
}

int main()
{
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);

    int a[4][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    int *ptr = (int *)(&a + 1);
    printf("%d,%d\n", *(*a + 1), *(ptr - 1));

    return 0;
}
