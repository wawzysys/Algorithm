#include <bits/stdc++.h>

using i64 = long long;

void solve() {
	i64 n, m;
	std::cin >> n >> m;
	if (n == m) {
		std::cout << n << " " << m << "\n";
	} else if (n > m) {
		i64 d = n - m;
		if (d < m) {
			std::cout << 2 * (n - m) << " " << 0 << "\n";
		} else if (d == m) {
			std::cout << m << " " << m << "\n";
		} else {
			std::cout << n << " " << n - 2 * m << "\n";
		}
	} else {
		std::swap(n, m);
		i64 d = n - m;
		if (d < m) {
			std::cout << 0 << " " << 2 * (n - m) << "\n";
		} else if (d == m) {
			std::cout << m << " " << m << "\n";
		} else {
			std::cout << n - 2 * m << " " << n << "\n";
		}
	}
}

int main() {
	std::cin.sync_with_stdio(false);
	std::cin.tie(0);

	solve();

	return 0;
}
N = p1 ^ c1 * p2 ^ c2 ... * pk ^ ck
count = (c1 + 1)* (c2 + 1 ) 。。。(ck + 1) 