#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long x;
    cin >> x;

    int count = 0;
    long long i = x;

    while (i != 1)
    {
        if (i == 3)
        {
            count += 2;
            break;
        }

        if (i % 2 != 0)
        {

            if (((i + 1) / 2) % 2 == 0)
            {
                i++;
            }
            else
            {

                i--;
            }
            count++;
        }
        i /= 2;
        count++;
    }

    cout << count;
}
