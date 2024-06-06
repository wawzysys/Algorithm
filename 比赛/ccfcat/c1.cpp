#include <bits/stdc++.h>

using i64 = long long;


void solve() {
	i64 n, m;
	std::cin >> n >> m;
	std::vector<i64> p;
	i64 now = 1;
	while (now <= m) {
		p.push_back(now);
		now *= n + 1;
	}
	std::vector<std::array<i64, 2>> ans;
	int len = p.size();

	for (int i = len - 1; i >= 0; --i) {
		if (p[i] <= m) {
			ans.push_back({m / p[i], i});
			m %= p[i];
		}
	}

	for (int i = 0; i < ans.size(); ++i) {
		auto [x, y] = ans[i];
		if (i) std::cout << "+";
		if (x == 1) {
			if (y > 1) {
				std::cout << "x^" << y;
			} else if (y == 1) {
				std::cout << "x";
			} else {
				std::cout << x;
			}
		} else {
			if (y > 1) {
				std::cout << x << "x^" << y;
			} else if (y == 1) {
				std::cout << x << "x";
			} else {
				std::cout << x;
			}
		}
	}
}

int main() {
	std::cin.sync_with_stdio(false);
	std::cin.tie(0);

	solve();

	return 0;
}