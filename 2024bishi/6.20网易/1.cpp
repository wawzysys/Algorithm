#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> a(5), b(5), c(5), d(5);
    for (int i = 0; i < 5; ++i)
    {
        cin >> a[i];
    }
    for (int i = 0; i < 5; ++i)
    {
        cin >> b[i];
    }
    for (int i = 0; i < 5; ++i)
    {
        cin >> c[i];
    }
    for (int i = 0; i < 5; ++i)
    {
        cin >> d[i];
    }

    int op = 0, idx1 = 0, idx2 = 0;

    while (idx1 < 5 && idx2 < 5)
    {
        if (op % 2 == 0)
        {
            d[idx2] -= a[idx1];
            if (d[idx2] <= 0)
            {
                idx2++;
            }
        }
        else
        {
            b[idx1] -= c[idx2];
            if (b[idx1] <= 0)
            {
                idx1++;
            }
        }
        op++;
    }

    if (idx1 < 5)
    {
        int ans = 5 - idx1;
        cout << "win" << endl;
        cout << ans << endl;
    }
    else
    {
        int ans = 5 - idx2;
        cout << "lose" << endl;
        cout << ans << endl;
    }

    return 0;
}
