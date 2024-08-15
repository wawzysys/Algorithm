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
void solve() {
    const int  N = 2e5 + 10;
    DSU uf(N);
    cin >> n;
    int idx = 0;
    map<int, int> mp;
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
class TreeAncestor {
    std::vector<int> depth;
    std::vector<std::vector<int>> pa;
public:
    TreeAncestor(std::vector<std::pair<int, int>> &edges) {
        int n = edges.size() + 1;
        int m = 32 - __builtin_clz(n); // n 的二进制长度
        
        std::vector<std::vector<int>> g(n);
        for (auto [x, y]: edges) { // 节点编号从 0 开始
            g[x].push_back(y);
            g[y].push_back(x);
        }

        depth.resize(n);
        pa.resize(n, std::vector<int>(m, -1));
        std::function<void(int, int)> dfs = [&](int x, int fa) {
            pa[x][0] = fa;
            for (int y: g[x]) {
                if (y != fa) {
                    depth[y] = depth[x] + 1;
                    dfs(y, x);
                }
            }
        };
        dfs(0, -1);

        for (int i = 0; i < m - 1; i++)
            for (int x = 0; x < n; x++)
                if (int p = pa[x][i]; p != -1)
                    pa[x][i + 1] = pa[p][i];
    }

    int get_kth_ancestor(int node, int k) {
        for (; k; k &= k - 1)
            node = pa[node][__builtin_ctz(k)];
        return node;
    }

    // 返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
    int get_lca(int x, int y) {
        if (depth[x] > depth[y])
            std::swap(x, y);
        // 使 y 和 x 在同一深度
        y = get_kth_ancestor(y, depth[y] - depth[x]);
        if (y == x)
            return x;
        for (int i = pa[x].size() - 1; i >= 0; i--) {
            int px = pa[x][i], py = pa[y][i];
            if (px != py) {
                x = px;
                y = py;
            }
        }
        return pa[x][0];
    }
};