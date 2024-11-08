#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;
int n, m;
vector<int> a;
template <typename T>
vector<T> input()
{
    vector<T> list;
    string input;
    getline(cin, input);
    istringstream stream(input);
    T number;
    while (stream >> number)
    {
        list.push_back(number);
    }
    return list;
}
bool check(int limit, const vector<int> &a)
{
    int l = 0;     
    int r = n - 1;
    int need = 0;  
    while (l <= r)
    {
        if (a[l] + a[r] <= limit)
        {
            l++;
        }
        r--;
        need++;
    }

    return m >= need;
}
int main()
{
    cin >> m;
    cin.ignore();
    a = input<int>();
    n = a.size();
    sort(a.begin(), a.end());
    int l = a[n - 1];
    int r = a[n - 2] + a[n - 1];
    int ans = r;
    while (l <= r)
    {
        int mid = (l + r) >> 1;
        if (check(mid, a))
        {
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
        }
    }
    cout << l << endl;
    return 0;
}
