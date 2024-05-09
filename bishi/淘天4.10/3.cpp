#include <bits/stdc++.h>
using namespace std;

const int N = 1E5 + 10;
int p[N], s[N];

int find(int x) {
    if (p[x] != x) {
        p[x] = find(p[x]);
    }
    return p[x];
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        p[i] = i;
        s[i] = 1;
    }
    set<pair<int, int>> st;
    while (m--) {
        int x, y;
        cin >> x >> y;
        if (st.count({min(x, y), max(x, y)})) {
            s[find(x)] = 3;
            printf("No\n");
        } else {
            st.insert({min(x, y), max(x, y)});
            int px = find(x), py = find(y);
            if (px != py) {
                int t1 = min(s[px], s[py]);
                int t2 = max(s[px], s[py]);
                if (t1 == 1 && t2 == 1) {
                    printf("No\n");
                    p[px] = py;
                } else if (t1 == 1 && t2 == 2) {
                    printf("Yes\n");
                    p[px] = py;
                    s[py] = 2;
                } else {
                    p[px] = py;
                    s[py] = 3;
                    printf("No\n");
                }
            } else {
                if (s[px] == 1) {
                    s[px] = 2;
                    printf("Yes\n");
                } else if (s[px] == 2) {
                    s[px] = 3;
                    printf("No\n");
                } else {
                    printf("No\n");
                }
            }
        }
    }
    
    return 0;
}