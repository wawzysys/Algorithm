#include <stdio.h>

int main() {
    int n, q;
    if(scanf("%d %d", &n, &q) != 2) {
        return 1;
    }
    
    int prices[n];
    for (int i = 0; i < n; i++) {
        if(scanf("%d", &prices[i]) != 1) {
            return 1;
        }
    }
    
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
        if(scanf("%d %d", &type, &x) != 2) {
            return 1;
        }
        
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
                
                if (dp[x]) {
                    printf("Yes\n");
                } else {
                    printf("No\n");
                }
            }
        } else if (type == 2) {
            selected[x - 1] = 1;
            if (prices[x - 1] == maxPrice) {
                maxPrice = 0;
                for (int j = 0; j < n; j++) {
                    if (selected[j] == 0) {
                        maxPrice += prices[j];
                    }
                }
            }
        }
    }
    
    return 0;
}