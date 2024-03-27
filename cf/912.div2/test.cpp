#include<bits/stdc++.h>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<map>
#include<queue>
#include<vector>
#define pa pair< int , int >
using namespace std;

inline int read()
{
   int x=0,f=1;char ch=getchar();
   while (!isdigit(ch)){if (ch=='-') f=-1;ch=getchar();}
   while (isdigit(ch)){x=(x<<1)+(x<<3)+ch-'0';ch=getchar();}
   return x*f;
}

const int maxn = 1e5+1e2;
const int maxm = 4e6+1e2;

int point[maxn],nxt[maxm],to[maxm],val[maxm];
int n,m;
int vis[maxn],dis[maxn];
int cnt;
int s,t;
priority_queue<pa,vector<pa>,greater<pa> > q;

void addedge(int x,int y,int w)
{
    nxt[++cnt]=point[x];
    to[cnt]=y;
    val[cnt]=w;
    point[x]=cnt;
}

int c;

void dijkstra(int s)
{
    memset(dis,127/3,sizeof(dis));
    memset(vis,0,sizeof(vis));
    dis[s]=0;
    q.push(make_pair(0,s));
    while (!q.empty())
    {
        int x = q.top().second;
        q.pop();
        if (vis[x]) continue;
        vis[x]=1;
        for (int i=point[x];i;i=nxt[i])
        {
            int p = to[i];
            if (dis[p]>dis[x]+val[i])
            {
                dis[p]=dis[x]+val[i];
                q.push(make_pair(dis[p],p));
            }
        }
    }
}

int main()
{
  cin >> n >> m >> c;
  for (int i=1;i<=m;++i)
  {
     int x=read(),y=read(),w=read();
     addedge(x,y,w);
  }
  for (int i=0;i<=n;++i)
  {
     for (int j=1;j<=n;j<<=1)
     {
        int tmp = (i^j);
        if (tmp>n) continue;
        addedge(i,tmp,j*c);
       }
  }
  cin>>s>>t;
  dijkstra(s);
  cout<<dis[t]<<endl;
  return 0;
}
