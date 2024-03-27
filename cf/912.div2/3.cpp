#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    //     if (scanf("%d %d", &n, &q) != 2) {
    //     // fprintf(stderr, "Input error!\n");
    //     return 1;
    // }
    cin >> n >> q;
    int prices[n];
    for (int i = 0; i < n; i++)  cin >> prices[i];
    int selected[n];
    for (int i = 0; i < n; i++) {
        selected[i] = 0;
    }
    
    int maxPrice = 0;
    for (int i = 0; i < n; i++) {
        if (selected[i] == 0) {
            maxPrice += prices[i];
        }
    }
    
    for (int i = 0; i < q; i++) {
        int type, x;
        cin >> type >> x;
        
        if (type == 1) {
            if (x > maxPrice) {
                printf("No\n");
            } else {
                int dp[x + 1];
                for (int j = 0; j <= x; j++) {
                    dp[j] = 0;
                }
                dp[0] = 1;
                
                for (int j = 0; j < n; j++) {
                    if (selected[j] == 0) {
                        for (int k = x; k >= prices[j]; k--) {
                            dp[k] |= dp[k - prices[j]];
                        }
                    }
                }
                
                if (dp[x]) cout << "Yes" << endl;
                 else cout << "No" << endl;
            }
        } else if (type == 2) {
            selected[x - 1] = 1;
            maxPrice -= prices[x - 1];  
            }
        }
    int mmm = 2;
    cout << 2 * mmm << endl;
    
    return 0;
}