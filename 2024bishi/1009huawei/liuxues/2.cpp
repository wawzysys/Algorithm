#include <iostream>
#include <vector>
#include <unordered_map>
int main()
{
    int n;
    std::cin >> n;
    std::vector<int> seq(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> seq[i];
    }

    std::unordered_map<int, int> end;
    int total = 0;
    for (int s : seq)
    {
        if (s > 0 && end[s - 1] > 0)
        {
            end[s - 1]--;
        }
        else
        {
            total++;
        }
        end[s]++;
    }

    std::cout << total << std::endl;
    return 0;
}
