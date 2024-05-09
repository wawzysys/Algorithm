#include <bits/stdc++.h>
int n, m, w;
using namespace std;
struct DSU {
    int count;
    std::vector<int> f, siz;
    DSU(int n) : count(n), f(n), siz(n, 1) { std::iota(f.begin(), f.end(), 0); }
    int leader(int x) {
        while (x != f[x]) x = f[x] = f[f[x]];
        return x;
    }
    bool same(int x, int y) { return leader(x) == leader(y); }
    bool merge(int x, int y) {
        x = leader(x);
        y = leader(y);
        if (x == y) return false;
        siz[x] += siz[y];
        f[y] = x;
        count -= 1;
        return true;
    }
    int size(int x) { return siz[leader(x)]; }
};
map<int, int> mp;
void solve() {
    const int  N = 1e5 + 10;
    DSU uf(N);
    cin >> n;
    int idx = 0;
    vector<vector<int>> a;
    while(n --) {
        int i, j, e;
        cin >> i >> j >> e;
        if(mp.find(i) == mp.end()) mp[i] = idx++;
        if(mp.find(j) == mp.end()) mp[j] = idx++; 
        if(e == 1){
            uf.merge(mp[i], mp[j]);
        }else{
            a.push_back({mp[i], mp[j]});
        }
    }
    for(auto  &t : a){
        int i = t[0], j = t[1];
        if(uf.same(i, j)){
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
    return ;
}
int main() {
    std::cin.sync_with_stdio(false);
    std::cin.tie(0);
    int t;
    cin >> t;
    while(t -- )
    solve();

    return 0;
}
