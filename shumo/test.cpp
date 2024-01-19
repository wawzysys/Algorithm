#include<bits/stdc++.h>
using namespace std;
string a;
int cnt;
int main(){
	getline(cin, a);
	for(int i = 0; i < a.size(); i ++ ){
		if(a[i] >= 48 && a[i] <= 57) 
			cnt ++;

	}
	cout << cnt << endl;
	return 0;
}