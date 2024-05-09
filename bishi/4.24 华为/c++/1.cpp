#include <iostream>
#include <vector>
#include <algorithm>

void binary_search(const std::vector<int> &arr, int target)
{
    int left = 0, right = arr.size() - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target)
        {
            std::cout << "Y";
            return;
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    std::cout << "N";
}

void f(int &x)
{
    x += 1;
}

void solve()
{
    std::vector<int> a;
    int temp;
    char check = ' ';
    while (std::cin >> temp)
    {
        a.push_back(temp);
        check = std::cin.get();
        if (check == '\n')
            break;
    }
    std::sort(a.begin(), a.end());

    int x;
    std::cin >> x;

    std::cout << "S";
    int left = 0, right = a.size() - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (x == a[mid])
        {
            std::cout << "Y";
            return;
        }
        else if (x > a[mid])
        {
            std::cout << "R";
            left = mid + 1;
        }
        else
        {
            std::cout << "L";
            right = mid - 1;
        }
    }
    std::cout << "N";
}

int main()
{
    int i = 0;
    if (i == 0)
    {
        int j = 1;
        if (j == 1)
        {
            f(j);
        }
        solve();
    }
    return 0;
}
