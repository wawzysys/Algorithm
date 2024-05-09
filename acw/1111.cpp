#include<bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
#define LL long long

int p[N];
int find(int u) {
	return p[u] == u ? u : p[u] = find(p[u]);
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int n;
	cin >> n;

	for(int i = 1; i <= n; i++) p[i] = i;
	vector<int> cnt(n + 1);
	for(int i = 1; i <= n; i++) cnt[i] = 1;
	for(int i = 1; i <= n; i++) {
		int x;
		cin >> x;
		int pi = find(i), px = find(x);
		if(pi != px) {
			p[px] = pi;
			cnt[pi] += cnt[px];
		}
	}
	LL ans = n;
	for(int i = 1; i <= n; i++) {
		if(find(i) == i) {
			ans += 1LL * cnt[i] * (cnt[i] - 1);
		}
	}
	cout << ans;


	return 0;
}