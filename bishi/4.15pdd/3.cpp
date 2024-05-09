#include <iostream>
#include <vector>
#include <climits> // For INT_MAX

using namespace std;

int main() {
    int t, n;
    cin >> t;

    while (t--) {
        cin >> n;
        vector<int> a(n + 1); 
        int k = 0;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            k += a[i];
        }

        int min1 = INT_MAX, sum = 0;
        for (int i = 1; i * i <= k; i++) {
            if (k % i == 0) {
                int ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == k / i) {
                        max1 = max(max1, ans);
                        ans = 0;
                        cnt = 0;
                    }
                }
                if (cnt == 0 && max1 <= min1) {
                    sum = k / i;
                    min1 = max1;
                }
                ans = 0, cnt = 0, max1 = 0;
                for (int j = 1; j <= n; j++) {
                    cnt += a[j];
                    ans++;
                    if (cnt == i) {
                        max1 = max(max1, ans);
                        cnt = 0;
                        ans = 0;
                    }
                }
                if (cnt == 0 && max1 < min1) {
                    sum = i;
                    min1 = max1;
                }
            }
        }

        cout << min1 << " " << sum << endl;
    }

    return 0;
}
