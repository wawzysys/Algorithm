#include <bits/stdc++.h>
using namespace std;

int main()
{
    string line;
    getline(cin, line);
    vector<int> arr;
    string num;
    stringstream ss(line);
    while (ss >> num)
    {
        arr.push_back(stoi(num));
    }

    int K;
    cin >> K;

    int window_size = 0;
    for (auto &x : arr)
    {
        if (x < K)
        {
            window_size++;
        }
    }
    if (window_size <= 1)
    {
        cout << "0" << endl;
        return 0;
    }
    int good = 0;
    for (int i = 0; i < window_size; i++)
    {
        if (arr[i] < K)
        {
            good++;
        }
    }
    int max_good = good;
    for (int i = window_size; i < arr.size(); i++)
    {
        if (arr[i - window_size] < K)
        {
            good--;
        }

        if (arr[i] < K)
        {
            good++;
        }
        if (good > max_good)
        {
            max_good = good;
        }
    }
    int min_swaps = window_size - max_good;
    cout << min_swaps << endl;

    return 0;
}
