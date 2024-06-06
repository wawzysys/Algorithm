#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
int n, m;
int max1 = 0;
int dx[] = {0, 1, 0, -1}, dy[] = {1, 0, -1, 0};
int a[6][6] = {10};
void pp()
{
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void dfs(int x, int y, int b[][6])
{
	// for(int i=1;i<=n;i++)
	// 	{
	// 		for(int j=1;j<=m;j++)
	// 		{
	// 			cout<<a[i][j]<<" ";
	// 		}
	// 		cout<<endl;
	// 	}
	int a[6][6];
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
		{
			a[i][j] = b[i][j];
		}
	int st[6][6];
	int cnt = 0;
	int sum = 0;
	queue<pii> q;
	q.push({x, y});
	memset(st, 0, sizeof(st));
	st[x][y] = 1;
	while (q.size())
	{
		pii t = q.front();
		q.pop();
		sum++;
		for (int i = 0; i < 4; i++)
		{
			int xx = t.first + dx[i], yy = t.second + dy[i];
			if (xx >= 1 && xx <= n && yy >= 1 && yy <= m && st[xx][yy] != 1 && a[xx][yy] == a[t.first][t.second])
			{
				q.push({xx, yy});
				st[xx][yy] = 1;
			}
		}
	}
	if (sum >= 3)
	{
		cnt++;
		for (int i = n; i >= 1; i--)
		{
			for (int j = m; j >= 1; j--)
			{
				if (st[i][j] == 1)
				{
					a[i][j] = -1;
				}
			}
		}
		for (int i = n; i >= 1; i--)
		{
			for (int j = m; j >= 1; j--)
			{
				int k = i;
				while (a[k + 1][j] == -1)
				{
					a[k + 1][j] = a[k][j];
					a[k][j] = -1;
					k++;
				}
			}
		}
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] != -1)
				{
					dfs(i, j, a);
				}
				for (int i = 1; i <= n; i++)
				{
					for (int j = 1; j <= m; j++)
					{
						cout << a[i][j] << " ";
					}
					cout << endl;
				}
				cout << endl;
			}
		}
	}
	if (cnt == 0)
	{
		int res = 0;
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				if (a[i][j] == -1)
				{
					res++;
				}
			}
		}
		max1 = max(max1, res);
	}
}
int main()
{
	cin >> n >> m;
	int a[6][6];
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> a[i][j];
		}
	}
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			dfs(i, j, a);
			// 				for(int i=1;i<=n;i++)
			// {
			// 	for(int j=1;j<=m;j++)
			// 	{
			// 		cout<<a[i][j]<<" ";
			// 	}
			// 	cout<<endl;
			// }
			// cout << endl;
		}
		// 	for(int i=1;i<=n;i++)
		// {
		// 	for(int j=1;j<=m;j++)
		// 	{
		// 		cout<<a[i][j]<<" ";
		// 	}
		// 	cout<<endl;
		// }
		// cout << endl;
	}
	cout << max1;
}