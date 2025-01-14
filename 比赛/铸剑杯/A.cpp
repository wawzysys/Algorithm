#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;
    // Calculate k, the position of the middle element
    ll k = (n * n + 1) / 2;

    ll left = 1;
    ll right = n * n;
    ll answer = 0;

    while (left <= right)
    {
        ll mid = left + (right - left) / 2;
        // Count the number of elements <= mid in the multiplication table
        ll count = 0;
        for (ll i = 1; i <= n; ++i)
        {
            // To prevent division by zero and ensure correctness
            if (i > mid)
            {
                break;
            }
            count += min((ll)n, mid / i);
        }
        if (count >= k)
        {
            answer = mid;
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    cout << answer;
}
