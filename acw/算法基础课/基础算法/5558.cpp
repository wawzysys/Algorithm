#include<bits/stdc++.h>
using  namespace std;
int a[110];
int main(){
	int n, k;
	cin >> n >> k;
	for(int i = 0; i < n; i ++ ) cin >> a[i];
	cout << a[k - 1];
	return 0;

}