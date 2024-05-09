#include<cstdio>
#include<iostream>
#include<climits>
#include<algorithm>
#include<cmath>
using namespace std;
int s[55][55][55];
int inf=0x3f3f3f3f;
int f(int n,int m,int p){
	if(n*m==p || p==0){
		return 0;
	}
	if(n>m){
		swap(n,m);
	}
	if(s[n][m][p]>0){
		return s[n][m][p];
	}
	int smin=inf;
	for(int i=1;i<=n/2;i++){
		for(int j=0;j<=p;j++){
			int ans=m*m+f(i,m,j)+f(n-i,m,p-j);
			smin=min(ans,smin);
		}
	}
	for(int i=1;i<=m/2;i++){
		for(int j=0;j<=p;j++){
			int ans=n*n+f(i,n,j)+f(m-i,n,p-j);
			smin=min(smin,ans);
		}
	}
	return s[n][m][p]=smin;
}
int main(){
	int T,n,m,p;
	scanf("%d",&T);
	while(T--){
		scanf("%d %d %d",&n,&m,&p);
		printf("%d\n",f(n,m,p));
	}
return 0;
}