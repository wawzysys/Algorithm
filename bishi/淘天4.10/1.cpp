#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin >> t;
	while(t -- ){
		int n, k;
		cin >> n >> k;
		map<int, int> mp;
		vector<pair<int, int>> a;
		for(int i = 0; i < n; i ++ ){
			int a_i;
			cin  >> a_i;
			mp[a_i] ++;
		}
		for (auto [u, v] : mp){
			a.push_back({v, u});
		}
		sort(a.begin(), a.end(), greater<pair<int, int>>());
		int ans = 0, last = n, cnt = 0;
		for(auto[u, v] : a){
			// cout << v <<  endl;
			if(last + cnt * u >= k){
				ans = max(v, ans);
			}
			last -= u;
			cnt ++;
			cout << last << endl;
		}
		printf("%d\n", ans);
	}
	return 0;
}