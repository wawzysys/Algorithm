#include<bits/stdc++.h>
#pragma GCC optimize("Ofast")
#define INF 0x3f3f3f3f
#define IOS ios::sync_with_stdio(false);cin.tie(0);
#define int long long
#define pb push_back
#define vct vector
#define checkbit __builtin_popcount
#define gcd __gcd
#define use int T;cin>>T;while(T--)
#define LEN length()
#define all(a) a.begin(),a.end() 
// template<class T> bool mmax(T &u, T v) { return u < v ? (u = v, 1) : 0; }
template<class T> bool mmin(T &u, T v) { return u > v ? (u = v, 1) : 0; }
#define lowbit(x) (x&(-x))
#define yes cout<<"YES"<<'\n'
#define no cout<<"NO"<<'\n'
using namespace std;
typedef pair<int,int>pii;
signed main()
{IOS
use{
   string a;cin>>a;
   int cnt=0;
   int _1=-1,_0=-1;
   for(int i=0;i<a.LEN;i++){
       if(a[i]=='0'){cnt++;_0=i;}
       else _1=i;
   }
   if(cnt==(a.LEN-cnt))cout<<"0"<<endl;
   else if(_1==-1||_0==-1)cout<<a.LEN<<endl;
   else {
       int ans=0;
       if(cnt>a.LEN-cnt){
           int t=a.LEN-cnt;
          for(int i=0;i<a.LEN;i++){
              if(a[i]=='0'&&t>0)t--;
              if(t==0){
                  if(i+1<a.LEN&&a[i+1]!='1')
                  {ans=a.LEN-i-1;
                  break;}
              }
          }
       }
        if(cnt<a.LEN-cnt){
           int t=cnt;
           
          for(int i=0;i<a.LEN;i++){
              if(a[i]=='1'&&t>0)t--;
              if(t==0){
                 if(i+1<a.LEN&&a[i+1]!='0')
                  {ans=a.LEN-i-1;
                  break;}
              }
          }
       }
          cout<<ans<<endl;
   }
}
return 0;
}