#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

// Define a structure for projects
struct Project {
    ll a; // start date
    ll b; // end date
    ll p; // reward
};

// Comparator to sort projects by end date
bool cmp(const Project &x, const Project &y){
    if(x.b != y.b)
        return x.b < y.b;
    return x.a < y.a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    ll n;
    cin >> n;
    vector<Project> projects(n);
    for(auto &proj : projects){
        cin >> proj.a >> proj.b >> proj.p;
    }
    
    // Sort projects by end date
    sort(projects.begin(), projects.end(), cmp);
    
    // Create an array of end times
    vector<ll> end_times(n);
    for(int i=0;i<n;i++) end_times[i] = projects[i].b;
    
    // Initialize dp array
    // To save space, use a vector and keep updating
    // dp[i] represents the maximum reward up to the i-th project
    // Using 1-based indexing
    vector<ll> dp(n+1, 0);
    dp[0] = 0;
    
    for(int i=1;i<=n;i++){
        // For projects[i-1], find the last j where end_times[j-1] < projects[i-1].a
        // Use upper_bound to find the first end_time >= a, then subtract 1
        ll a_i = projects[i-1].a;
        // upper_bound returns the first index where end_time > a_i -1, i.e., >= a_i
        int j = upper_bound(end_times.begin(), end_times.begin()+i-1, a_i -1) - end_times.begin();
        // dp[j] is the maximum reward up to project j
        dp[i] = max(dp[i-1], dp[j] + projects[i-1].p);
    }
    
    cout << dp[n];
}
