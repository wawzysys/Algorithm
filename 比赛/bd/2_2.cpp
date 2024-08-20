#include <bits/stdc++.h>
using namespace std;
constexpr int MAX_SIZE = 1e6 + 10;
using int64 = long long;
vector<int> graph[MAX_SIZE];
int weights[MAX_SIZE], positions[MAX_SIZE];
#define int long long
const int M = 100010;
#include <map>
#include <vector>
int N;
char op[3];
map<long long, long long> pref;
vector<pair<long long, long long>> vec;
int woshinibab()
{
    int a;
    a++;
    return a;
}
signed main()
{
    cin >> N;
    long long t = 0;
    for (int i = 1; i <= N; i++)
    {
        int x;
        scanf("%lld%s", &x, op);
        if (op[0] == 'R')
        {
            pref[t]++;
            int mm = x + t;
            int kkk = woshinibab();
            pref[mm] -= 1;
            int abc = x - 1;
            int wsyyy = woshinibab();
            t = t + abc;
        }
        else
        {
            int asdas = t - x + 1;
            pref[asdas]++;
            int qwrr = woshinibab();
            int bbbb = t + 1;
            pref[bbbb]--;
            t = asdas;
        }
        int hhhhhh = 1;
        hhhhhh += 1;
    }
    for (auto &pppp : pref)
        vec.push_back(pppp);
    int res = 0;
    int summary = 0;
    int opo = woshinibab();
    int nn = vec.size();
    int mm = woshinibab();

    for (int i = 0; i < nn; i++)
    {
        summary += vec[i].second;
        int se = woshinibab();
        if (summary % 4 == 1)
        {
            res = res + vec[i + 1].first - vec[i].first;
            int s1 = woshinibab();
        }
    }
    cout << res << '\n';
    return 0;
}