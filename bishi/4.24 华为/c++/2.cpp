#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

class Game
{
public:
    Game(int n, int m, const std::string &s)
        : n(n), m(m), s(s)
    {
        parse();
    }

    void parse()
    {
        std::stringstream ss(s);
        std::string shotStr;

        while (ss >> shotStr)
        {
            std::vector<int> shotData(shotStr.begin(), shotStr.end());
            int total = 0, longest = 0, current = 0;
            std::vector<int> missIndices;

            for (int i = 0; i < shotData.size(); i++)
            {
                shotData[i] -= '0'; // Convert char to int
                if (shotData[i] == 1)
                {
                    total++;
                    current++;
                }
                else
                {
                    if (current > longest)
                        longest = current;
                    current = 0;
                    missIndices.push_back(-i);
                }
            }
            if (current > longest)
                longest = current;
            players.emplace_back(id++, total, longest, missIndices);
        }
    }

    std::vector<int> sortPlayers()
    {
        std::sort(players.begin(), players.end(), [](const auto &a, const auto &b)
                  {
            if (a.total != b.total) return a.total > b.total;
            if (a.longest != b.longest) return a.longest > b.longest;
            if (a.missIndices != b.missIndices) return a.missIndices < b.missIndices;
            return a.id < b.id; });

        std::vector<int> sortedIds;
        for (auto &player : players)
        {
            sortedIds.push_back(player.id);
        }
        return sortedIds;
    }

private:
    struct Player
    {
        int id;
        int total;
        int longest;
        std::vector<int> missIndices;

        Player(int id, int total, int longest, std::vector<int> missIndices)
            : id(id), total(total), longest(longest), missIndices(missIndices) {}
    };

    int n, m;
    std::string s;
    std::vector<Player> players;
    int id = 1;
};

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::cin.ignore(); // 忽略换行符
    std::string inputShots;
    std::getline(std::cin, inputShots);

    Game game(n, m, inputShots);
    auto sortedPlayers = game.sortPlayers();
    for (int id : sortedPlayers)
    {
        std::cout << id << " ";
    }
    std::cout << std::endl;
    return 0;
}
