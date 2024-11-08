#include <iostream>
using namespace std;
int main()
{
    int n, q;
    cin >> n >> q;
    int *a = new int[n + 1];
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < q; i++)
    {
        int op, l, r;
        cin >> op >> l >> r;

        int res = a[l];
        int idx = l + 1;
        bool isAnd;

        if (op == 1)
        {
            isAnd = true;
        }
        else
        {
            isAnd = false;
        }
        while (idx <= r)
        {
            if (isAnd)
            {
                res = res & a[idx];
            }
            else
            {
                res = res | a[idx];
            }
            isAnd = !isAnd;
            idx++;
        }

        cout << res << endl;
    }
    delete[] a;
    return 0;
}
