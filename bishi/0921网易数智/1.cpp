#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    string lineA;
    getline(cin, lineA);
    string lineB;
    getline(cin, lineB);
    vector<int> A;
    int num;
    ll sumA = 0;
    stringstream ssA(lineA);
    while (ssA >> num)
    {
        A.push_back(num);
        sumA += num;
    }

    stringstream ssB(lineB);
    ll min_s = 0;
    ll cur_s = 0;
    int i = 0;
    while (ssB >> num && i < A.size())
    {
        int D = num - A[i];
        cur_s += D;
        if (cur_s < min_s)
        {
            min_s = cur_s;
        }
        if (cur_s > 0)
        {
            cur_s = 0;
        }
        i++;
    }

    ll ans = sumA + min_s;
    if (min_s >= 0)
    {
        ans = sumA;
    }

    cout << ans;
}
