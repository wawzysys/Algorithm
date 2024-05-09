#include <iostream>
#include <vector>
#include <queue>
#include <functional>

template <typename T>
std::vector<T> nsmallest(const std::vector<T> &data, std::size_t n)
{
    if (n >= data.size())
    {
        std::vector<T> result(data.begin(), data.end());
        std::sort(result.begin(), result.end());
        return result;
    }
    std::priority_queue<T> pq;
    for (const auto &item : data)
    {
        pq.push(item);
        if (pq.size() > n)
        {
            pq.pop();
        }
    }
    std::vector<T> result;
    while (!pq.empty())
    {
        result.push_back(pq.top());
        pq.pop();
    }
    std::sort(result.begin(), result.end());
    return result;
}

int main()
{
    std::vector<int> data = {5, 3, 8, 1, 2, 7, 4, 6};
    std::size_t n = 3;

    std::vector<int> result = nsmallest(data, n);

    for (int value : result)
    {
        std::cout << value << " ";
    }
    return 0;
}
