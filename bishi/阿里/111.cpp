#include <iostream>
#include <stack>
#include <vector>
const int MAXN = 100010;
const int MAXP = 10000010;
int a[MAXN];
std::vector<int> prime;
std::vector<bool> st(MAXP, false);
std::stack<long long> s;

bool check(long long x) {
    if (x <= MAXP) {
        return !st[x];
    } else {
        for (size_t j = 0; prime[j] <= x / prime[j]; j++) {
            if (x % prime[j] == 0) return false;
        }
        return true;
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    st[1] = true;
    for (int i = 2; i <= MAXP; i++) {
        if (!st[i]) {
            prime.push_back(i);
            for (int j = 0; j < prime.size() && prime[j] <= MAXP / i; j++) {
                st[i * prime[j]] = true;
                if (i % prime[j] == 0) break;
            }
        }
    }
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        std::cin >> a[i];
        long long now = a[i];
        while (!s.empty() && check(s.top()) && check(now)) {
            now += s.top();
            s.pop();
        }
        s.push(now);
    }

    std::cout << s.size() << std::endl;

    return 0;
}
