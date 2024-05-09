#include<bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
int q[N];
int quick_sort(int q[], int l, int r, int k){
	if(l == r) return q[k];
	int x = q[(l + r) >> 1];
	int i = l - 1, j = r + 1;
	while(i < j){
		do i ++; while(q[i] < x);
		do j --; while(q[j] > x);
		if(i < j) swap(q[i] ,q[j]);
	}
	int sl = j - l + 1;
	if(k > j){
		return quick_sort(q, j + 1, r, k);
	}else{
		return quick_sort(q, l, j, k);
	}
}
int main(){
	int n, k;
	cin >> n >> k;
	for(int i = 0; i < n; i ++ ) cin  >> q[i];
	cout << quick_sort(q, 0, n - 1, k - 1);
	return 0;

}