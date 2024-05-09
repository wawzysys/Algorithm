#include <iostream>
#include <vector>
using namespace std;

template <typename T>
struct Fenwick {
    int n;
    vector<T> a;
    
    Fenwick(int n_ = 0) {
        init(n_);
    }
    
    void init(int n_) {
        n = n_;
        a.assign(n + 1, T{0}); // Ensuring 1-based index.
    }
    
    void add(int x, const T& v) {
        for (int i = x; i <= n; i += i & -i) {
            a[i] += v;
        }
    }
    
    T sum(int x) {
        T result = T{};
        for (int i = x; i > 0; i -= i & -i) {
            result += a[i];
        }
        return result;
    }
    
    T rangeSum(int l, int r) {
        return sum(r) - sum(l - 1);
    }
};

const int N = 100010;
Fenwick<long long> tr1(N);
Fenwick<long long> tr2(N);
int a[N];

int main() {
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        cin >> a[i];
        int b = a[i] - a[i - 1];
        tr1.add(i, b);
        tr2.add(i, (long long)(b) * i);
    }
    
    while(m--) {
        string op;
        int l, r;
        cin >> op >> l >> r;
        if(op == "Q") {
            cout << tr1.sum(r) * (r + 1) - tr2.sum(r) - (tr1.sum(l - 1) * l - tr2.sum(l - 1)) << endl;
        } else  {
            int c;
            cin >> c;
            tr1.add(l, c);
            tr2.add(l, (long long)(c) * l);
            tr1.add(r + 1, -c);
            tr2.add(r + 1, (long long)(-c) * (r + 1));
        }
    }
    return 0;
}
