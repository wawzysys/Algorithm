#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;
using PII = std::pair<int, int>;
const int N = 1e5 + 13;

int main()
{

    int data[][4] = {1, 2, 3, 4, 5, 6, 7, 8};
    int *data_ptr = &data[0][1];
    printf("%d \n", data_ptr[2]);

    return 0;
}
