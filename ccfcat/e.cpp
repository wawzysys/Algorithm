#include<bits/stdc++.h>
using namespace std;
std::vector<int> minp, primes;
bool st[20000005];
int cnt[20000005];
void seive(int n) {
	minp.assign(n + 1, 0);
	primes.clear();

	for (int i = 2; i <= n; ++i) {
		if (minp[i] == 0) {
			minp[i] = i;
			primes.push_back(i);
			st[i]=1;
		}

		for (auto p : primes) {
			if (i * p > n) {
				break;
			}
			minp[i * p] = p;
			if (i%p==0) {
				break;
			}
		}
	}
}
int main()
{
	int n;
	int summ=0;
	cin>>n;
	seive(n);
	for(int i=0;i<primes.size();i++)
	{
		int sum=0;
		if(st[primes[i]]==1&&n!=primes[i]&&st[n-primes[i]]!=1)
		{
			sum=1;
			int k=n-primes[i];
			for(int j=0;primes[j]<=k/primes[j];j++)
			{
				if(k%primes[j]==0)
				{
					int s=0;
					while(k%primes[j]==0)
					{
						s++;
						k/=primes[j];
					}
					sum*=(s+1);
				}
			}
			if(k>1) sum*=2;
		}
		summ+=sum;
	}
	cout<<summ;
}
