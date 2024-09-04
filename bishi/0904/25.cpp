#include <bits/stdc++.h>

const int inf = 0x3f3f3f3f;
using i64 = long long;
using PII = std::pair<int, int>;
const int N = 1e5 + 13;

void add(int *value)
{
    *value = 1;
}

void add(int &value)
{
    value += 2;
}
int main()
{

    int a = 0;
    add(a);
    printf(" a=%d \n", a);
    add(&a);
    printf("a=%d \n", a);
    return 0;
}