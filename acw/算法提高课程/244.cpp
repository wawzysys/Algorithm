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
    int select(const T& k) {
    int x = 0;
    T cur{};
    // __lg函数计算的是以2为底的对数，这里通过这个值确定最大的权重位
    for (int i = 1 << std::__lg(n); i > 0; i /= 2) {
        if (x + i <= n && cur + a[x + i] <= k) {
            cur += a[x + i];
            x += i;
        }
    }
    return x; // 返回的x是最小的索引，其前缀和大于等于k
}

};

const int N = 100010;
Fenwick<long long> tr1(N);
int a[N];

int main() {
    int n;
    cin >> n;
    vector<int> b;
    for(int i = 1; i < n; i ++ ){
        cin >> a[i];
    }
    for(int i = 1; i <= N; i ++){
        tr1.add(i, 1);
    }
    for(int i = n - 1; i >= 0; i -- ){
        int l = 0, r = n + 1;
        while(l <= r){
            int mid = l + r >> 1;
            if(tr1.sum(mid) >=( a[i] + 1)){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        tr1.add(l, - 1);
        b.push_back(l);
    }
    for(int i = b.size() - 1; i >= 0; i -- ){

        cout << b[i] << " \n"[i != 0];
    }

    
    return 0;
}
