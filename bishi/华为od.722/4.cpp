#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;
int n;
vector<int> requirements;
int m;
template <typename T>
vector<T> input()
{
    vector<T> list;
    string input;
    getline(cin, input);
    istringstream stream(input);
    int number;
    while (stream >> number)
    {
        list.push_back(number);
    }
    return list;
}

int main()
{
    cin >> m;
    cout << m << endl;
    cin.ignore();
    vector<int> requirements = input<int>();
    n = requirements.size();
    cout << n << endl;
    sort(requirements.begin(), requirements.end());
    for (int x : requirements)
    {
        cout << x << " ";
    }
    return 0;
}
